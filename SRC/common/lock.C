// -*- C++ -*-
// $RCSfile: lock.C,v $
// $Revision: 1.29 $
// $Author: langer $
// $Date: 2011/03/30 20:39:10 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */


#include <oofconfig.h>
#include <pthread.h>
#include <iostream>
#include <errno.h>
#include "lock.h"
#include "ooferror.h"
#include "threadstate.h"

static bool enabled = true;

bool disable_all() {
  bool oldval = enabled;
  enabled = false;
  return oldval;
}

void enable_all() {
  enabled = true;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

Lock::Lock() {
  if(enabled) 
    pthread_mutex_init(&lock, NULL);
}

Lock::~Lock() {
  if(enabled)
    pthread_mutex_destroy(&lock);
}


void Lock::acquire() {
  if(enabled) {
    if(mainthread_query()) {
      std::cerr << "Lock::acquire called on main thread. " << this << std::endl;
      throw ErrProgrammingError("Lock error.", __FILE__, __LINE__);
    }
    pthread_mutex_lock(&lock);
  }
}

void SLock::acquire() {
  if(enabled) {
    pthread_mutex_lock(&lock);
  }
}

void Lock::release() {
  if(enabled)
    pthread_mutex_unlock(&lock);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// See
// https://computing.llnl.gov/tutorials/pthreads/#ConditionVariables
// for a good discussion of condition variables.  In particular:
// Proper locking and unlocking of the associated mutex variable is
// essential when using these routines. For example:
//  * Failing to lock the mutex before calling pthread_cond_wait() may
//    cause it NOT to block.
//  * Failing to unlock the mutex after calling pthread_cond_signal()
//    may not allow a matching pthread_cond_wait() routine to complete
//    (it will remain blocked).


Condition::Condition(Lock *lock)
  : lock(lock)
{
  if(enabled)
    pthread_cond_init(&condition, NULL);
}

Condition::~Condition() {
  if(enabled)
    pthread_cond_destroy(&condition);
}

// Condition::wait() releases the lock and blocks the current thread
// until Condition::broadcast is called in some other thread.  Then it
// reacquires the lock and unblocks.

void Condition::wait() {
  if(enabled) {
    pthread_cond_wait(&condition, &lock->lock);
  }
}

void Condition::broadcast() {
  if(enabled)
    pthread_cond_broadcast(&condition);
}

void Condition::signal() {
  if(enabled)
    pthread_cond_signal(&condition);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

RWLock::RWLock()
  : r(0), w(0), p(0)
{
  if(enabled) {
    pthread_mutex_init(&local_lock, NULL);
    pthread_cond_init(&rw_zero, NULL);
  }
}

RWLock::~RWLock() {
  if(enabled) {
    pthread_mutex_destroy(&local_lock);
    pthread_cond_destroy(&rw_zero);
  }
}


// Before you can write, you have to wait until there are no 
// readers or writers.  
void RWLock::write_acquire() {
  if(enabled) {
    if(mainthread_query()) {
      std::cerr << "RWLock::write_acquire called on main thread." << std::endl;
      throw ErrProgrammingError("RWLock write error.", __FILE__, __LINE__);
    }
    pthread_mutex_lock(&local_lock);
    while (r>0 || w>0 || p>0) {
      pthread_cond_wait(&rw_zero, &local_lock);
    }
    w=1;
    pthread_mutex_unlock(&local_lock);
  }
}


void RWLock::write_release() {
  if(enabled) {
    pthread_mutex_lock(&local_lock);
    w = 0;
    p = 0;
    pthread_cond_broadcast(&rw_zero);  // r==0 at this point.
    pthread_mutex_unlock(&local_lock);
  }
}


// You cannot read if anybody is writing.  Other readers are OK.
void RWLock::read_acquire() {
  if(enabled) {
    if(mainthread_query()) {
      std::cerr << "RWLock::read_acquire called on main thread." << std::endl;
      throw ErrProgrammingError("RWLock read error.", __FILE__, __LINE__);
    }
    pthread_mutex_lock(&local_lock);
    while (w>0) {
      pthread_cond_wait(&rw_zero, &local_lock);
    }
    r++;
    pthread_mutex_unlock(&local_lock);
  }
}

void RWLock::read_release() {
  if(enabled) {
    pthread_mutex_lock(&local_lock);
    r--;
    if (r==0) { // w==0 is already true here.
      assert(w == 0);
      pthread_cond_broadcast(&rw_zero);
    }
    pthread_mutex_unlock(&local_lock);
  }
}

void RWLock::write_pause() {
  if(enabled) {
    bool ok = true;
    pthread_mutex_lock(&local_lock);
    // It's an error to call write_pause when not writing, but an
    // exception can't be thrown until after local_lock has been
    // released, so the state is stored in 'ok'.
    ok = (w != 0);
    p = 1;
    w = 0;
    pthread_cond_broadcast(&rw_zero);
    pthread_mutex_unlock(&local_lock);
    if(!ok) {
      // throwing ErrProgrammingError here seems to be unreliable, so
      // we're using an assert statement as well.
      assert(ok);
      throw ErrProgrammingError("Called RWLock::write_pause() when not writing",
				__FILE__, __LINE__);
    }
  }
}

void RWLock::write_resume() {
  if(enabled) {
    pthread_mutex_lock(&local_lock);
    while (r>0) {
      //std::cerr << "***** Waiting in RWLock::write_resume" << std::endl;
      pthread_cond_wait(&rw_zero, &local_lock);
    }
    p = 0;
    w = 1;
    pthread_mutex_unlock(&local_lock);
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// SRWLock functions -- same as RWLock except for error-checking.


// Before you can write, you have to wait until there are no 
// readers or writers.  
void SRWLock::write_acquire() {
  if(enabled) {
    pthread_mutex_lock(&local_lock);
    while (r>0 || w>0 || p>0) {
      pthread_cond_wait(&rw_zero, &local_lock);
    }
    w=1;
    pthread_mutex_unlock(&local_lock);
  }
}


// You cannot read if anybody is writing.  Other readers are OK.
void SRWLock::read_acquire() {
  if(enabled) {
    pthread_mutex_lock(&local_lock);
    while (w>0) {
      pthread_cond_wait(&rw_zero, &local_lock);
    }
    r++;
    pthread_mutex_unlock(&local_lock);
  }
}


KeyHolder::KeyHolder(Lock &some_lock, bool verbose)
  : lock(&some_lock), verbose(verbose)
{
  if(enabled)
    lock->acquire();
}


KeyHolder::~KeyHolder() {
  if(enabled)
    lock->release();
  if(verbose)
    std::cerr << "KeyHolder::~KeyHolder: released " << lock << std::endl;
  
}

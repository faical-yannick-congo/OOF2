// -*- C++ -*-
// $RCSfile: meshiterator.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2010/05/27 20:38:59 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MESHITERATOR_SWG
#define MESHITERATOR_SWG

%module meshiterator
%include "engine/typemaps.swg"

%extern "engine/element.swg"
%pragma(python) code="from ooflib.SWIG.engine.element import ElementPtr"
%extern "engine/node.swg"
%pragma(python) code="from ooflib.SWIG.engine.node import NodePtr"
%pragma(python) code="from ooflib.SWIG.engine.node import FuncNodePtr"

%{
#include "engine/meshiterator.h"
%}

// Constructors for these classes aren't swigged because the objects
// should only be created by calling FEMesh::node_iterator, etc.

// TODO: Make these into real Python iterators.  next() must return
// the object being pointed to, and they must have an __iter__
// function that returns self.

class NodeIterator {
public:
  // NodeIterator();		// DON'T SWIG THE CONSTRUCTOR
  ~NodeIterator();
  bool end();
  int size();
  Node *node();
  %addmethods {
    void next() {
      ++(*self);
    }
  }
};

class FuncNodeIterator {
public:
  // FuncNodeIterator();		// DON'T SWIG THE CONSTRUCTOR
  ~FuncNodeIterator();
  bool end();
  int size();
  FuncNode *node();
  %addmethods {
    void next() {
      ++(*self);
    }
  }
};

class ElementIterator {
public:
  // ElementIterator(); 		// DON'T SWIG THE CONSTRUCTOR
  ~ElementIterator();
  bool end();
  int size();
  int count();
  Element *element();
  %addmethods {
    void next() {
      ++(*self);
    }
  }
};

#endif // MESHITERATOR_SWG

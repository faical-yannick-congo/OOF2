// -*- C++ -*-
// $RCSfile: nonmaxSuppression.h,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modifed
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef NONMAXSUPPRESSION_H
#define NONMAXSUPPRESSION_H

class DoubleArray;
class BoolArray;

DoubleArray nonmaxSuppress(const DoubleArray&,const IntArray&);

#endif // NONMAXSUPPRESSION_H	

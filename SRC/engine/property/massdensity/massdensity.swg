// -*- C++ -*-
// $RCSfile: massdensity.swg,v $
// $Revision: 1.15 $
// $Author: langer $
// $Date: 2010/04/13 15:40:50 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef MASSDENSITY_SWG
#define MASSDENSITY_SWG

%module massdensity

%{
#include "engine/property/massdensity/massdensity.h"
%}
%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"

class MassDensityProp : public Property {
public:
  MassDensityProp(PyObject *self, char *, double);
};

%pragma(python) include="massdensity.spy"

#endif // MASSDENSITY_SWG

# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.1 $
# $Author: langer $
# $Date: 2010/03/08 16:36:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
from ooflib.common import utils

def noExecution():
    # The file with the syntax error shouldn't have run.  If it did,
    # then the main OOF namespace contains a variable 'borogoves'.
    try:
        utils.OOFeval('borogoves')
    except NameError:
        return True
    

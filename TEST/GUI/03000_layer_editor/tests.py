# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.4 $
# $Author: langer $
# $Date: 2014/09/27 21:42:10 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
from layereditortests import *

def sensitivityCheck0():
    return sensitizationCheck(
        {"NewLayer": 1,
         "Send": 0,
         "DisplayMethods:New": 0,
         "DisplayMethods:Edit": 0,
         "DisplayMethods:Copy": 0,
         "DisplayMethods:Delete": 0
        },
        base="OOF2 Graphics Layer Editor")

def sensitivityCheck1():
    return sensitizationCheck(
        {"NewLayer": 1,
         "Send": 0,
         "DisplayMethods:New": 1,
         "DisplayMethods:Edit": 0,
         "DisplayMethods:Copy": 0,
         "DisplayMethods:Delete": 0
        },
        base="OOF2 Graphics Layer Editor")

def sensitivityCheck2():
    return sensitizationCheck(
        {"NewLayer": 1,
         "Send": 1,
         "DisplayMethods:New": 1,
         "DisplayMethods:Edit": 1,
         "DisplayMethods:Copy": 1,
         "DisplayMethods:Delete": 1
        },
        base="OOF2 Graphics Layer Editor")

def sensitivityCheck3():
    return sensitizationCheck(
        {"NewLayer": 1,
         "Send": 1,
         "DisplayMethods:New": 1,
         "DisplayMethods:Edit": 1,
         "DisplayMethods:Copy": 0,
         "DisplayMethods:Delete": 0
        },
        base="OOF2 Graphics Layer Editor")


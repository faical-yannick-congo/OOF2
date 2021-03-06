# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.4 $
# $Author: langer $
# $Date: 2014/09/27 21:41:48 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def skeletonBdySensitizationCheck0():
    return sensitizationCheck(
        {'New' : 1,
         'Modify' : 0,
         'Rename' : 0,
         'Delete' : 0
         },
        base='OOF2:Skeleton Boundaries Page:Pane:Boundaries')

def skeletonBdySensitizationCheck1():
    return sensitizationCheck(
        {'New' : 1,
         'Modify' : 1,
         'Rename' : 1,
         'Delete' : 1
         },
        base='OOF2:Skeleton Boundaries Page:Pane:Boundaries')
    

def skeletonBdySizeCheck(skeleton, bdyname, size):
    from ooflib.common.IO import whoville
    sc = whoville.getClass('Skeleton')[skeleton]
    bdy = sc.getBoundary(bdyname)
    return bdy.current_size() == size

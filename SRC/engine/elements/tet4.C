// -*- C++ -*-
// $RCSfile: tet4.C,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:08 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "engine/masterelement.h"
#include "tet4shapefunction.h"
#include "common/trace.h"


// Master element for the four node tetrahedron:


class Tet4MasterElement : public TetrahedralMaster {
public:
  Tet4MasterElement()
    : TetrahedralMaster("T4_4",
			  "Isoparametric 4 noded tetrahedron with linear interpolation for both fields and positions.", 4, 1)
  {
    shapefunction = new Tet4ShapeFunction(*this);
    mapfunction = shapefunction;

    ProtoNode *pn0 = addProtoNode(MasterCoord(0.0, 0.0, 0.0));
    pn0->set_mapping();
    pn0->set_func();
    pn0->set_corner();
    pn0->on_edge(0);
    pn0->on_edge(2);
    pn0->on_edge(3);

    ProtoNode *pn1 = addProtoNode(MasterCoord(0.0, 1.0, 0.0));
    pn1->set_mapping();
    pn1->set_func();
    pn1->set_corner();
    pn1->on_edge(0);
    pn1->on_edge(1);
    pn1->on_edge(4);

    ProtoNode *pn2 = addProtoNode(MasterCoord(1.0, 0.0, 0.0));
    pn2->set_mapping();
    pn2->set_func();
    pn2->set_corner();
    pn2->on_edge(1);
    pn2->on_edge(2);
    pn2->on_edge(5);
    
    ProtoNode *pn3 = addProtoNode(MasterCoord(0.0, 0.0, 1.0));
    pn3->set_mapping();
    pn3->set_func();
    pn3->set_corner();
    pn3->on_edge(3);
    pn3->on_edge(4);
    pn3->on_edge(5);

    addSCpoint(MasterCoord(1./4, 1./4, 1./4));
  }
  virtual ~Tet4MasterElement() {
    delete shapefunction;   
  }

  int map_order() const {
    return 1;
  }
  int fun_order() const {
    return 1;
  }

};

void tet4init() {
  static Tet4MasterElement m;
}


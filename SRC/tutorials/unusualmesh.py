# -*- python -*-
# $RCSfile: unusualmesh.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2014/09/27 21:41:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.tutorials import tutorial
TutoringItem = tutorial.TutoringItem
TutorialClass = tutorial.TutorialClass

TutorialClass(
    subject = "Nonrectangular Domain",
    ordering=5,
    lessons = [
    
    TutoringItem(
    subject="Introduction",
    comments=

    """Meshes (Skeletons) that are generated by OOF2 are always
    RECTANGULAR.  However, it doesn't mean that
    you're limited only to a rectangular domain.
    
    OOF2 allows you to simulate arbitrarily shaped problem domains by
    selectively assigning materials to a Microstructure.

    In this tutorial, we will cover this topic in detail.
    """),

    TutoringItem(
    subject="Microstructure",
    comments=
    
    """Open a graphics window, if none has been opened yet, with
    the BOLD(Graphics/New) command in the BOLD(Windows) menu.

    Locate the file BOLD(el_shape.png) within the
    share/oof2/examples directory in your OOF2 installation.
    
    Open the BOLD(Microstructure) page and click BOLD(New from Image
    File) to create a new microstructure.  In the file selection
    dialog box, navigate to BOLD(el_shape.png).  Click BOLD(OK) to
    load the Image and create the Microstructure.

    """,
    signal = ("new who", "Microstructure")
    ),
    
    TutoringItem(
    subject="Categorizing Pixels",
    comments=

    """The microstructure features BOLD(green) and BOLD(ivory) regions.
    We're interested only in the BOLD(green) region -- our problem
    domain will be an BOLD(L)-shaped bracket, so to speak.

    To categorize pixels automatically,
    open the BOLD(Image) page and click the BOLD(Group) button.
    
    Go back to the BOLD(Microstructure) page and you will see that
    BOLD(2) pixel groups have been created for the microstructure.
    """ ),

    TutoringItem(
    subject="Pixel Group",
    comments=

    """Now, we'll change names of pixel groups for our convenience.

    Go to the BOLD(Microstructure) page and select the first pixel group,
    which represents BOLD(green) pixels.
    Click the BOLD(Rename) button.

    Replace the old name with "green".  (Triple-clicking on the old
    name in the dialog box will select the whole name, making it
    easier to replace.)

    Don't bother with the other pixel group, since we're not going to
    use it.
    """,
    
    signal="renamed pixel group"),

    TutoringItem(
    subject="Material",
    comments=
    """Open the BOLD(Materials) page.
    Create a new material by clicking on the BOLD(New) button in the
    BOLD(Material) pane.

    Click the check box for non-generic name, and type BOLD(green-material)
    in the text entry field.
    Click BOLD(OK).
    """,
    signal="new_material"
    ),

    TutoringItem(
    subject="Property",
    comments=

    """Start creating a property for BOLD(green-material) by selecting
    BOLD(Isotropic) from BOLD(Mechanical->Elasticity)
    in the property hierarchy.

    Click BOLD(Copy) and check the box to give it a user-defined name.

    Check the box and type in BOLD(green_elasticity). Click
    BOLD(OK).""",

    signal = "new property"
    ),

    TutoringItem(
    subject="Parametrizing Property",
    comments=
    
    """Select BOLD(green_elasticity) from the Property hierarchy and
    either double click it or click the BOLD(Parametrize...) button to
    input actual values.

    The elasticity parameters can be entered in a variety of formats.
    The default format is BOLD(Cij).  Change it to BOLD(E and nu) with
    the pull down menu at the top of the Parametrize dialog box.

    Set the modulus of elasticity (BOLD(young)) to 1.0 and Poisson's ratio
    (BOLD(poisson)) to 0.3.

    Click BOLD(OK) to finish up.
    """,
    signal = "redraw"
    ),

    TutoringItem(
    subject="Adding Property to Material",
    comments=

    """Select BOLD(green_elasticity) from the Property tree.

    Click BOLD(Add Property to Material) from the bottom of
    the BOLD(Property) pane to add the Property to the Material.

    The addition should immediately appear in the BOLD(Material) pane,
    in the list of Properties below the Material selector.
    """,
    signal= "prop_added_to_material"
    ),

    TutoringItem(
    subject="Assigning Material to Pixels",
    
    comments=
    
    """Select the material BOLD(green-material) and click on the
    button labelled BOLD(Assign Material to Pixels...) in the
    BOLD(Material) pane.

    The pop-up window lets you choose the Microstructure to which the
    Material will be assigned (currently we only have one,
    "el_shape.png"), and the pixels within the Microstructure.  Choose
    the pixel group BOLD(green) in the BOLD(pixels) pull-down menu.

    Click BOLD(OK) to finish.

    We will NOT do anything for the BOLD(ivory) pixels.
    """,
    signal = "materials changed in microstructure"
    ),

    TutoringItem(
    subject="Skeleton",
    comments=

    """Go to the BOLD(Skeleton) page.
    Click BOLD(New...) to create an initial skeleton.

    Use these  values for the initial skeleton: BOLD(x_elements) = 20,
    BOLD(y_elements) = 20, and BOLD(skeleton_geometry)=QuadSkeleton.
    Click BOLD(OK) to create the Skeleton.
    """,
        
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Boundary Modification",
    comments=

    """Since we're only interested in the BOLD(green) portion of the
    Skeleton, we're going to modify the existing boundaries.  The
    existing boundaries include edges of non-green elements.
    
    Let us modify two edge boundaries, BOLD(top) and BOLD(right), so that
    only the segments from the BOLD(green) elements will be part of them.
    Advance to the next slide for real action.
    """
    ),

    TutoringItem(
    subject="Boundary Modification 1",
    comments=

    """ Go to the BOLD(Skeleton Boundaries) page. Select the BOLD(top)
    boundary from the BOLD(Boundaries) pane. Now, if you go to the
    graphics window, you will see that the selected edge boundary is
    displayed.  What we're going to do is to remove segments from the
    BOLD(ivory) elements from this boundary.

    Open the BOLD(Skeleton Selection) toolbox in the graphics window.
    Select BOLD(Segment) from the selection modes. Choose BOLD(Rectangle)
    for the selection method. Now, try to select all the segments
    that belong to BOLD(ivory) elements from the BOLD(top) boundary
    by click-and-dragging the mouse.

    Selected segments appear as thick BOLD(green) lines.  Go back to
    the BOLD(Skeleton Boundaries) page and click the BOLD(Modify...)
    button. Select BOLD(Remove segments) for the modifying method and
    select BOLD(<selection>) for BOLD(group).  Click BOLD(OK). You
    should see the immediate change in the BOLD(Boundary data) pane
    and in the graphics window.  """,
        
    signal = "new boundary configuration"
    ),

    TutoringItem(
    subject="Boundary Modification 2",
    comments=

    """We'll do a similar thing for the BOLD(right) edge boundary.
    Select the BOLD(right) boundary from the BOLD(Boundaries) pane.

    Go to the graphics window and try to select all the segments
    that belong to BOLD(ivory) elements from the BOLD(right) boundary.

    Go back to the BOLD(Skeleton Boundaries) page and click the
    BOLD(Modify...) button. Select BOLD(Remove segments) for the
    modifying method and select BOLD(<selection>) for the BOLD(group).
    Click BOLD(OK).

    Now, we're ready to create a Mesh from this Skeleton.
    """,
        
    signal = "new boundary configuration"
    ),
    
    TutoringItem(
    subject="Finite Element Mesh",
    comments=
    """Open the BOLD(FE Mesh) page.

    Click the BOLD(New) button to get a dialog box for creating a new
    Mesh.  Here you must specify which types of mesh elements to use
    for triangular (BOLD(element3)) and quadrilateral (BOLD(element4))
    skeleton elements and their orders.

    Use these values, BOLD(mapping order) = 2, BOLD(interpolation order) = 2,
    BOLD(3-sided element) = T6_6, BOLD(4-sided element) = Q8_8 to create
    a quadratic Mesh.

    Click BOLD(OK).

    As you recall, we didn't assign any material to the BOLD(ivory)
    elements.  These elements will be dummies, which makes the Mesh
    (even if it's rectangular) an effective L-shaped domain.  If you
    hide or delete the BOLD(Skeleton) layer in the BOLD(Graphics)
    window, you'll see that Mesh elements are drawn only where a
    Material has been assigned.

    Now, let us solve a problem using this Mesh.
    """,
    signal = ("new who", "Mesh")
    ),

    TutoringItem(
    subject=" Field",
    comments=

    """Proceed to the BOLD(Fields) page.
    
    Check all BOLD(three) boxes for the BOLD(Displacement) field.
    """,
    signal = "field activated"
    ),

    TutoringItem(
    subject="Activating Equations",
    comments=

    """Open the BOLD(Equations) page.

    We're solving a BOLD(Force_Balance) equation,
    so check the corresponding box.
    """,
    signal = "equation activated"
    ),

    TutoringItem(
    subject="Boundary Conditions",
    comments="""Go to the BOLD(Boundary Conditions) page.

    The boundary conditions (all BOLD(Dirichlet)) we're going to apply are:

    BOLD(1.) u_x = 0 on the BOLD(left) side
    
    BOLD(2.) u_y = 0 on the BOLD(left) side

    BOLD(3.) u_x = 0 on the BOLD(top) side

    BOLD(4.) u_y = 0 on the BOLD(top) side

    BOLD(5.) u_y = -2 on the BOLD(right) side"""
    ),

    TutoringItem(
    subject="Boundary Condition 1",
    comments=
    """Click the BOLD(New...) button from the BOLD(Condition) pane to bring
    up a boundary condition builder.  The pull-down menu at the top of
    the dialog box allows you to choose the type of boundary
    condition.  Set it to BOLD(Dirichlet), which
    gives associated Fields fixed values at the boundaries.
    
    Since only one Field is defined and only one Equation is active,
    the BOLD(field) and BOLD(equation) menus have only one choice
    each.  Leave them set to BOLD(Displacement) and
    BOLD(Force_Balance).
 
    The first B.C. deals with displacement in the BOLD(x)-direction,
    so select BOLD(x) for both BOLD(Displacement) and
    BOLD(Force_Balance).

    The BOLD(profile) is the functional form of the Field along the
    boundary.  Set BOLD(profile) to BOLD(Constant Profile) with BOLD(value) = 0.

    Choose the BOLD(boundary) to which this condition should
    be applied (BOLD(left)) and click BOLD(OK).
    """,
    signal = "boundary conditions changed"
    ),

    TutoringItem(
    subject="Boundary Condition 2-5",
    comments=
    """Create the rest of Boundary Conditions as you did for the first one.
    You can always go back to previous slides to check some numbers and
    stuff by clicking on the BOLD(Back) button. BUT, make sure
    to create all the BCs before you move on to the next slide.

    (If you get back to this page and discover that the BOLD(Next)
    button is disabled, just edit one of the boundary conditions.  You
    don't actually have to change it, you just have to trick the
    tutorial machinery into thinking you've changed something.)""",
    
    signal = "boundary conditions changed"
    ),

    TutoringItem(
    subject="Solution",
    comments=
    
    """Open the BOLD(Solver) page and just click BOLD(Solve).
    The deformed Mesh will be displayed in the graphics window.

    By default, OOF2 doesn't display elements with no material defined in
    the output, which explains what you're seeing now.

    We've covered how you simulate arbitrary problem domains by
    selectively assigning Materials so far.
    
    Thanks for following the tutorial!
    """)
    
    ])
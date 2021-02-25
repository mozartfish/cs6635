# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

for i in range(16):
    # create a new 'Arrow'
    registration_arrow = 'Arrow' + str(i)
    arrow = Arrow(registrationName=registration_arrow)

    # Properties modified on arrow1
    arrow.TipResolution = 12

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    arrow1Display = Show(arrow, renderView1, 'GeometryRepresentation')
    arrow1Display.Orientation = [0.0, 0.0, 360 * i / 16]

    # trace defaults for the display properties.
    arrow1Display.Representation = 'Surface'
    arrow1Display.ColorArrayName = [None, '']
    arrow1Display.SelectTCoordArray = 'None'
    arrow1Display.SelectNormalArray = 'None'
    arrow1Display.SelectTangentArray = 'None'
    arrow1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    arrow1Display.SelectOrientationVectors = 'None'
    arrow1Display.ScaleFactor = 0.1
    arrow1Display.SelectScaleArray = 'None'
    arrow1Display.GlyphType = 'Arrow'
    arrow1Display.GlyphTableIndexArray = 'None'
    arrow1Display.GaussianRadius = 0.005
    arrow1Display.SetScaleArray = [None, '']
    arrow1Display.ScaleTransferFunction = 'PiecewiseFunction'
    arrow1Display.OpacityArray = [None, '']
    arrow1Display.OpacityTransferFunction = 'PiecewiseFunction'
    arrow1Display.DataAxesGrid = 'GridAxesRepresentation'
    arrow1Display.PolarAxes = 'PolarAxesRepresentation'

    # reset view to fit data
    renderView1.ResetCamera()

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Shrink'
    registration_shrink = 'Shrink' + str(i)
    shrink = Shrink(registrationName=registration_shrink, Input=arrow)

    # set active source
    SetActiveSource(shrink)

    # show data in view
    shrink1Display = Show(shrink, renderView1, 'UnstructuredGridRepresentation')
    shrink1Display.Orientation = [0.0, 0.0, 360 * i / 16]
    # trace defaults for the display properties.
    shrink1Display.Representation = 'Surface'
    shrink1Display.ColorArrayName = [None, '']
    shrink1Display.SelectTCoordArray = 'None'
    shrink1Display.SelectNormalArray = 'None'
    shrink1Display.SelectTangentArray = 'None'
    shrink1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    shrink1Display.SelectOrientationVectors = 'None'
    shrink1Display.ScaleFactor = 0.08833333253860474
    shrink1Display.SelectScaleArray = 'None'
    shrink1Display.GlyphType = 'Arrow'
    shrink1Display.GlyphTableIndexArray = 'None'
    shrink1Display.GaussianRadius = 0.0044166666269302365
    shrink1Display.SetScaleArray = [None, '']
    shrink1Display.ScaleTransferFunction = 'PiecewiseFunction'
    shrink1Display.OpacityArray = [None, '']
    shrink1Display.OpacityTransferFunction = 'PiecewiseFunction'
    shrink1Display.DataAxesGrid = 'GridAxesRepresentation'
    shrink1Display.PolarAxes = 'PolarAxesRepresentation'
    shrink1Display.ScalarOpacityUnitDistance = 0.33079247583139165
    shrink1Display.OpacityArrayName = [None, '']

    # show data in view
    shrink1Display = Show(shrink, renderView1, 'UnstructuredGridRepresentation')

    # hide data in view
    Hide(arrow, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(arrow)

    # create a new 'Extract Edges'
    registration_edges = 'ExtractEdges' + str(i)
    extractEdges = ExtractEdges(registrationName=registration_edges, Input=arrow)

    # show data in view
    extractEdges1Display = Show(extractEdges, renderView1, 'GeometryRepresentation')
    extractEdges1Display.Orientation = [0.0, 0.0, 360 * i / 16]
    # trace defaults for the display properties.
    extractEdges1Display.Representation = 'Surface'
    extractEdges1Display.ColorArrayName = [None, '']
    extractEdges1Display.SelectTCoordArray = 'None'
    extractEdges1Display.SelectNormalArray = 'None'
    extractEdges1Display.SelectTangentArray = 'None'
    extractEdges1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractEdges1Display.SelectOrientationVectors = 'None'
    extractEdges1Display.ScaleFactor = 0.1
    extractEdges1Display.SelectScaleArray = 'None'
    extractEdges1Display.GlyphType = 'Arrow'
    extractEdges1Display.GlyphTableIndexArray = 'None'
    extractEdges1Display.GaussianRadius = 0.005
    extractEdges1Display.SetScaleArray = [None, '']
    extractEdges1Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractEdges1Display.OpacityArray = [None, '']
    extractEdges1Display.OpacityTransferFunction = 'PiecewiseFunction'
    extractEdges1Display.DataAxesGrid = 'GridAxesRepresentation'
    extractEdges1Display.PolarAxes = 'PolarAxesRepresentation'

    # hide data in view
    Hide(arrow, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    # get layout
    layout1 = GetLayout()

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1422, 474)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.5, 0.0, 2.0076391311867505]
    renderView1.CameraFocalPoint = [0.5, 0.0, 0.0]
    renderView1.CameraParallelScale = 0.5196152428442091

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
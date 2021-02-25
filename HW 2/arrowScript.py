# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# create a new 'Arrow'
for i in range(16):
    registration_name = 'Arrow' + str(i)
    arrow = Arrow(registrationName=registration_name)
    arrow.TipResolution = 12
    arrow1Display = Show(arrow, renderView1, 'GeometryRepresentation')
    # Properties modified on arrow1Display
    arrow1Display.Orientation = [0.0, 0.0, 360 * i / 16]

# arrow1 = Arrow(registrationName='Arrow1')

# # Properties modified on arrow1
# arrow1.TipResolution = 12



# # show data in view
# arrow1Display = Show(arrow1, renderView1, 'GeometryRepresentation')

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

# Properties modified on arrow1Display
arrow1Display.Orientation = [0.0, 0.0, 90.0]

# Properties modified on arrow1Display.PolarAxes
arrow1Display.PolarAxes.Orientation = [0.0, 0.0, 90.0]

# # Properties modified on arrow1Display
# arrow1Display.Orientation = [0.0, 0.0, 360.0]

# Properties modified on arrow1Display.PolarAxes
arrow1Display.PolarAxes.Orientation = [0.0, 0.0, 360.0]

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1426, 1028)

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
# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
a2dvti = XMLImageDataReader(registrationName='2d.vti', FileName=['C:\\Users\\rajan\\Desktop\\cs6635\\HW 2\\data\\2d.vti'])
a2dvti.PointArrayStatus = ['Scalars_']

# Properties modified on a2dvti
a2dvti.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')

# trace defaults for the display properties.
a2dvtiDisplay.Representation = 'Slice'
a2dvtiDisplay.ColorArrayName = ['POINTS', 'Scalars_']
a2dvtiDisplay.LookupTable = scalars_LUT
a2dvtiDisplay.SelectTCoordArray = 'None'
a2dvtiDisplay.SelectNormalArray = 'None'
a2dvtiDisplay.SelectTangentArray = 'None'
a2dvtiDisplay.OSPRayScaleArray = 'Scalars_'
a2dvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a2dvtiDisplay.SelectOrientationVectors = 'None'
a2dvtiDisplay.ScaleFactor = 409.6
a2dvtiDisplay.SelectScaleArray = 'Scalars_'
a2dvtiDisplay.GlyphType = 'Arrow'
a2dvtiDisplay.GlyphTableIndexArray = 'Scalars_'
a2dvtiDisplay.GaussianRadius = 20.48
a2dvtiDisplay.SetScaleArray = ['POINTS', 'Scalars_']
a2dvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a2dvtiDisplay.OpacityArray = ['POINTS', 'Scalars_']
a2dvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a2dvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
a2dvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
a2dvtiDisplay.ScalarOpacityUnitDistance = 22.538152910782728
a2dvtiDisplay.ScalarOpacityFunction = scalars_PWF
a2dvtiDisplay.OpacityArrayName = ['POINTS', 'Scalars_']
a2dvtiDisplay.IsosurfaceValues = [100.0]
a2dvtiDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a2dvtiDisplay.ScaleTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a2dvtiDisplay.OpacityTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
a2dvtiDisplay.SliceFunction.Origin = [2048.0, 1024.0, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

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
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]
renderView1.CameraParallelScale = 2289.7336089597848

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
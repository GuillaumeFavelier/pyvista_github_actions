"""
Example PyVistaQt
=================
"""
import pyvista as pv
from pyvistaqt import BackgroundPlotter
p = BackgroundPlotter(line_smoothing=True)
p.add_mesh(pv.Cone(), smooth_shading=True)
p.enable_anti_aliasing()
p.enable_depth_peeling()

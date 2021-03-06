"""
Example PyVistaQt
=================
"""
import pyvista
from pyvistaqt import BackgroundPlotter

p = BackgroundPlotter(line_smoothing=True)
p.add_mesh(pyvista.Cone(), smooth_shading=True)
p.enable_anti_aliasing()
p.enable_depth_peeling()
p.show()

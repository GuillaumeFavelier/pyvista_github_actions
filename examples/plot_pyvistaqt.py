"""
Example 1
=========
"""
import pyvista as pv
from pyvistaqt import BackgroundPlotter
p = BackgroundPlotter()
p.add_mesh(pv.Cone())

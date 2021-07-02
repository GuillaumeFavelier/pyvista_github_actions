"""
Example 1
=========
"""
import pyvista as pv
pv.OFF_SCREEN = True
pv.BUILDING_GALLERY = True
p = pv.Plotter()
p.add_mesh(pv.Cone())
p.show()

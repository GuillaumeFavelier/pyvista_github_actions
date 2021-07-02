"""
Example PyVista
===============
"""
import pyvista
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True

p = pyvista.Plotter()
p.add_mesh(pyvista.Cone())
p.show()

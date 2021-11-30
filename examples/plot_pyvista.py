"""
Example PyVista
===============
"""
import pyvista

p = pyvista.Plotter()
p.add_mesh(pyvista.Cone())
p.show()

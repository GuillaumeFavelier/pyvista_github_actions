"""
Example PyVistaQt
=================
"""
import pyvista
from pyvistaqt import BackgroundPlotter
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True

p = BackgroundPlotter()
p.add_mesh(pyvista.Cone())
p.show()

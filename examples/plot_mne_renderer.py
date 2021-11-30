"""
Example MNE/Renderer
====================
"""
from mne.viz.backends import renderer
import pyvista
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True

# init scene
rend = renderer.create_3d_figure(
    size=(600, 600),
    bgcolor='grey',
    smooth_shading=False,
    scene=False,
)

rend.plotter.add_mesh(pyvista.Cone())

# use mesh
# import numpy as np
# tet_size = 1.0
# tet_x = np.array([0, tet_size, 0, 0])
# tet_y = np.array([0, 0, tet_size, 0])
# tet_z = np.array([0, 0, 0, tet_size])
# tet_indices = np.array([[0, 1, 2],
#                         [0, 1, 3],
#                         [0, 2, 3],
#                         [1, 2, 3]])
# tet_color = 'white'
# mesh_data = rend.mesh(
#     x=tet_x,
#     y=tet_y,
#     z=tet_z,
#     triangles=tet_indices,
#     color=tet_color,
# )
rend.show()

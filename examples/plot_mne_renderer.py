"""
Example MNE/Renderer
====================
"""
import numpy as np
import pyvista
from mne.viz.backends import renderer
pyvista.OFF_SCREEN = True

win_size = (600, 600)
win_color = 'grey'

tet_size = 1.0
tet_x = np.array([0, tet_size, 0, 0])
tet_y = np.array([0, 0, tet_size, 0])
tet_z = np.array([0, 0, 0, tet_size])
tet_indices = np.array([[0, 1, 2],
                        [0, 1, 3],
                        [0, 2, 3],
                        [1, 2, 3]])
tet_color = 'white'

# init scene
rend = renderer.create_3d_figure(
    size=win_size,
    bgcolor=win_color,
    smooth_shading=True,
    scene=False,
)
for interaction in ('terrain', 'trackball'):
    rend.set_interaction(interaction)

# use mesh
mesh_data = rend.mesh(
    x=tet_x,
    y=tet_y,
    z=tet_z,
    triangles=tet_indices,
    color=tet_color,
)
rend.show()

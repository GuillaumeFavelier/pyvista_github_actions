"""
Example MNE/Renderer
====================
"""
import numpy as np
from mne.viz.backends import renderer

# init scene
rend = renderer.create_3d_figure(
    size=(600, 600),
    bgcolor='grey',
    smooth_shading=False,
    scene=False,
)

# use mesh
tet_size = 1.0
tet_x = np.array([0, tet_size, 0, 0])
tet_y = np.array([0, 0, tet_size, 0])
tet_z = np.array([0, 0, 0, tet_size])
tet_indices = np.array([[0, 1, 2],
                        [0, 1, 3],
                        [0, 2, 3],
                        [1, 2, 3]])
tet_color = 'white'
mesh_data = rend.mesh(
    x=tet_x,
    y=tet_y,
    z=tet_z,
    triangles=tet_indices,
    color=tet_color,
)

rend.show()

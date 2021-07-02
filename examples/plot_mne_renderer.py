"""
Example MNE/Renderer
====================
"""
import numpy as np
import pyvista
from mne.viz.backends import renderer
pyvista.OFF_SCREEN = False

win_size = (600, 600)
win_color = 'black'

tet_size = 1.0
tet_x = np.array([0, tet_size, 0, 0])
tet_y = np.array([0, 0, tet_size, 0])
tet_z = np.array([0, 0, 0, tet_size])
tet_indices = np.array([[0, 1, 2],
                        [0, 1, 3],
                        [0, 2, 3],
                        [1, 2, 3]])
tet_color = 'white'

sph_center = np.column_stack((tet_x, tet_y, tet_z))
sph_color = 'red'
sph_scale = tet_size / 3.0

ct_scalars = np.array([0.0, 0.0, 0.0, 1.0])
ct_levels = [0.2, 0.4, 0.6, 0.8]
ct_surface = {
    "rr": sph_center,
    "tris": tet_indices
}

qv_color = 'blue'
qv_scale = tet_size / 2.0
qv_center = np.array([np.mean((sph_center[va, :],
                               sph_center[vb, :],
                               sph_center[vc, :]), axis=0)
                     for (va, vb, vc) in tet_indices])
center = np.mean(qv_center, axis=0)
qv_dir = qv_center - center
qv_scale_mode = 'scalar'
qv_scalars = np.linspace(1.0, 2.0, 4)

txt_x = 0.0
txt_y = 0.0
txt_text = "renderer"
txt_size = 14

cam_distance = 5 * tet_size

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
rend.remove_mesh(mesh_data)

# use contour
rend.contour(surface=ct_surface, scalars=ct_scalars,
             contours=ct_levels, kind='line')
rend.contour(surface=ct_surface, scalars=ct_scalars,
             contours=ct_levels, kind='tube')

# use sphere
rend.sphere(center=sph_center, color=sph_color,
            scale=sph_scale, radius=1.0)

# use quiver3d
kwargs = dict(
    x=qv_center[:, 0],
    y=qv_center[:, 1],
    z=qv_center[:, 2],
    u=qv_dir[:, 0],
    v=qv_dir[:, 1],
    w=qv_dir[:, 2],
    color=qv_color,
    scale=qv_scale,
    scale_mode=qv_scale_mode,
    scalars=qv_scalars,
)
# use tube
rend.tube(origin=np.array([[0, 0, 0]]),
          destination=np.array([[0, 1, 0]]))
tube = rend.tube(origin=np.array([[1, 0, 0]]),
                 destination=np.array([[1, 1, 0]]),
                 scalars=np.array([[1.0, 1.0]]))

# scalar bar
rend.scalarbar(source=tube, title="Scalar Bar",
               bgcolor=[1, 1, 1])

# use text
rend.text2d(x_window=txt_x, y_window=txt_y, text=txt_text,
            size=txt_size, justification='right')
rend.text3d(x=0, y=0, z=0, text=txt_text, scale=1.0)
rend.set_camera(azimuth=180.0, elevation=90.0,
                distance=cam_distance,
                focalpoint=center)
rend.reset_camera()
rend.show()

"""
Example MNE
===========
"""
import mne
import pyvista
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True

fname = mne.datasets.sample.data_path() + '/MEG/sample/sample_audvis_raw.fif'
raw = mne.io.read_raw_fif(fname)
mne.viz.plot_alignment(
    raw.info,
    subject='sample',
    surfaces=[]
)

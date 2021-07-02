"""
Example MNE
===========
"""
import mne
fname = mne.datasets.sample.data_path() + '/MEG/sample/sample_audvis_raw.fif'
raw = mne.io.read_raw_fif(fname)
mne.viz.plot_alignment(
    raw.info,
    subject='sample',
    surfaces=[]
)

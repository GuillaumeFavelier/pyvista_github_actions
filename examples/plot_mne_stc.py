"""
Example MNE/STC
===========
"""
import os
import mne
from mne.datasets import sample
import pyvista
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True

data_path = sample.data_path()
sample_dir = os.path.join(data_path, 'MEG', 'sample')
subjects_dir = os.path.join(data_path, 'subjects')
fname_stc = os.path.join(sample_dir, 'sample_audvis-meg')
stc = mne.read_source_estimate(fname_stc, subject='sample')
initial_time = 0.13
brain = stc.plot(subjects_dir=subjects_dir, initial_time=initial_time,
                 clim=dict(kind='value', lims=[3, 6, 9]),
                 size=600, background="white", hemi='lh')

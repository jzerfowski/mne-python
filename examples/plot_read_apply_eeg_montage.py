"""
==================================
Reading and applyting EEG Montages
==================================

"""
# Author: Denis Engemann <dneis.engemann@gmail.com>
#
# License: BSD (3-clause)

print(__doc__)

from mne import read_evokeds, rename_channels
from mne.datasets import sample
from mne.montages import read_montage, apply_montage

data_path = sample.data_path()

fname = data_path + '/MEG/sample/sample_audvis-ave.fif'
condition = 'Left Auditory'
evoked = read_evokeds(fname, condition=condition, baseline=(None, 0),
                      proj=True)

# Map channel names to montage
eeg_channels = [c for c in evoked.ch_names if c.startswith('EEG')]
names = ['%i' % int(k[-3:]) for k in eeg_channels]
rename_channels(evoked.info, dict(zip(eeg_channels, names)))

# Read montage and plot
montage = read_montage('M10', names)
montage.plot()

# Apply montage
apply_montage(evoked.info, montage)
evoked.plot_topomap(size=2, ch_type='eeg')

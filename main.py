# Description: This file is used to test the spectrogram plotting function
# Usage: python main.py

from utils import plot_spectrogram, plot_phase_spectrogram, plot_magnitude_and_phase_soectrogram, detect_instrument

# Load the audio file
path_guitar = 'all-samples/guitar/guitar_A2_very-long_forte_normal.mp3'
path_flute = 'all-samples/flute/flute_A4_1_forte_normal.mp3'
path_mandolin = 'all-samples/mandolin/mandolin_A3_very-long_forte_tremolo.mp3'
path_saxophone = 'all-samples/saxophone/saxophone_A3_1_forte_normal.mp3'

# Compute and plot the spectrogram
#plot_spectrogram(filepath_1)
#plot_spectrogram_from_path(filepath_2)
#plot_spectrogram_from_path(filepath_3)
#plot_spectrogram_from_path(filepath_4)

# Plot the phase spectrogram
#plot_phase_spectrogram(filepath_1)
# plot_phase_spectrogram(filepath_2)
# plot_phase_spectrogram(filepath_3)
# plot_phase_spectrogram(filepath_4)

# Plot the magnitude and phase spectrogram
plot_magnitude_and_phase_soectrogram(path_guitar)
plot_magnitude_and_phase_soectrogram(path_flute)
plot_magnitude_and_phase_soectrogram(path_mandolin)
plot_magnitude_and_phase_soectrogram(path_saxophone)

# Detect the instrument from the audio file
detect_instrument(path_guitar)
detect_instrument(path_flute)
detect_instrument(path_mandolin)
detect_instrument(path_saxophone)
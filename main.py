# Description: This file is used to test the spectrogram plotting function
# Usage: python main.py

from utils import plot_magnitude_and_phase_spectrogram, plot_chromagram, plot_mfcc, plot_waveform

# Load the audio file
path_guitar = 'all-samples/guitar/guitar_F4_very-long_forte_normal.mp3'
path_guitar2 = 'all-samples/guitar/guitar_G3_very-long_piano_normal.mp3'
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

# Plot the waveform
plot_waveform(path_guitar)
#plot_waveform(path_guitar2)
plot_waveform(path_flute)
#plot_waveform(path_mandolin)
#plot_waveform(path_saxophone)

# Plot the magnitude and phase spectrogram
plot_magnitude_and_phase_spectrogram(path_guitar)
#plot_magnitude_and_phase_spectrogram(path_guitar2)
plot_magnitude_and_phase_spectrogram(path_flute)
#plot_magnitude_and_phase_spectrogram(path_mandolin)
#plot_magnitude_and_phase_spectrogram(path_saxophone)

plot_chromagram(path_guitar)
#plot_chromagram(path_guitar2)
plot_chromagram(path_flute)
#plot_chromagram(path_mandolin)
#plot_chromagram(path_saxophone)

plot_mfcc(path_guitar)
#plot_mfcc(path_guitar2)
plot_mfcc(path_flute)
#plot_mfcc(path_mandolin)
#plot_mfcc(path_saxophone)

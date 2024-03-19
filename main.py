# Description: This file is used to test the spectrogram plotting function
# Usage: python main.py

from utils import plot_magnitude_and_phase_spectrogram, plot_spectrogram

# Load the audio file
path_guitar = 'all-samples/guitar/guitar_F4_very-long_forte_normal.mp3'
path_guitar2 = 'all-samples/guitar/guitar_G3_very-long_piano_normal.mp3'
path_guitar3 = 'all-samples/guitar/guitar_A2_very-long_piano_normal.mp3'

path_mandolin = 'all-samples/mandolin/mandolin_A3_very-long_forte_tremolo.mp3'
path_mandolin2 = 'all-samples/mandolin/mandolin_A4_very-long_piano_tremolo.mp3'
path_mandolin3 = 'all-samples/mandolin/mandolin_B5_very-long_piano_normal.mp3'

path_saxophone = 'all-samples/saxophone/saxophone_A3_1_forte_normal.mp3'
path_saxophone2 = 'all-samples/saxophone/saxophone_A4_long_forte_minor-trill.mp3'
path_saxophone3 = 'all-samples/saxophone/saxophone_As4_05_piano_normal.mp3'

path_flute = 'all-samples/flute/flute_A4_1_forte_normal.mp3'
path_flute2 = 'all-samples/flute/flute_A6_long_fortissimo_major-trill.mp3'
path_flute3 = 'all-samples/flute/flute_C4_05_mezzo-forte_normal.mp3'

'''

plot_magnitude_and_phase_spectrogram(path_guitar)
plot_magnitude_and_phase_spectrogram(path_guitar2)
plot_magnitude_and_phase_spectrogram(path_guitar3)

plot_magnitude_and_phase_spectrogram(path_mandolin)
plot_magnitude_and_phase_spectrogram(path_mandolin2)
plot_magnitude_and_phase_spectrogram(path_mandolin3)

plot_magnitude_and_phase_spectrogram(path_saxophone)
plot_magnitude_and_phase_spectrogram(path_saxophone2)
plot_magnitude_and_phase_spectrogram(path_saxophone3)

plot_magnitude_and_phase_spectrogram(path_flute)
plot_magnitude_and_phase_spectrogram(path_flute2)
plot_magnitude_and_phase_spectrogram(path_flute3)
'''

plot_spectrogram(path_guitar) #F4
plot_spectrogram(path_guitar2) #G3
plot_spectrogram(path_guitar3) #A2

plot_spectrogram(path_mandolin) #A3
plot_spectrogram(path_mandolin2) #A4
plot_spectrogram(path_mandolin3) #B5

plot_spectrogram(path_saxophone) #A3
plot_spectrogram(path_saxophone2) #A4
plot_spectrogram(path_saxophone3) #As4
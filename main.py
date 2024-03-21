# Description: This file is used to test the spectrogram plotting function
# Usage: python main.py

from utils import plot_magnitude_and_phase_spectrogram, plot_spectrogram

# Load the audio file
path_guitar = 'all-samples/guitar/guitar_B3_very-long_piano_normal.mp3'
path_guitar2 = 'all-samples/guitar/guitar_B4_very-long_piano_normal.mp3'
#path_guitar3 = 'all-samples/guitar/guitar_A2_very-long_piano_normal.mp3'

path_mandolin = 'all-samples/mandolin/mandolin_B3_very-long_piano_normal.mp3'
path_mandolin2 = 'all-samples/mandolin/mandolin_B4_very-long_piano_normal.mp3'
#path_mandolin3 = 'all-samples/mandolin/mandolin_B5_very-long_piano_normal.mp3'

path_saxophone = 'all-samples/saxophone/saxophone_B3_1_forte_normal.mp3'
path_saxophone2 = 'all-samples/saxophone/saxophone_B4_1_forte_normal.mp3'
#path_saxophone3 = 'all-samples/saxophone/saxophone_As4_05_piano_normal.mp3'

path_flute = 'all-samples/flute/flute_B4_1_forte_normal.mp3'
path_flute2 = 'all-samples/flute/flute_B5_1_forte_normal.mp3'
#path_flute3 = 'all-samples/flute/flute_C4_05_mezzo-forte_normal.mp3'

path_cello = 'all-samples/cello/cello_B3_1_mezzo-piano_arco-normal.mp3'
path_cello2 = 'all-samples/cello/cello_B5_1_mezzo-piano_arco-normal.mp3'

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

#plot_spectrogram(path_guitar) #B3
#plot_spectrogram(path_guitar2) #B4

#plot_spectrogram(path_mandolin) #B3
#plot_spectrogram(path_mandolin2) #B4

#plot_spectrogram(path_saxophone) #B3
#plot_spectrogram(path_saxophone2) #B5
#plot_spectrogram(path_saxophone3) #As4

plot_spectrogram(path_flute) #B4
#plot_spectrogram(path_flute2) #B5
#plot_spectrogram(path_flute3) #C4

#plot_spectrogram(path_cello) #B3
#plot_spectrogram(path_cello2) #B5

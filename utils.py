import librosa
import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram(path):

    # Load the audio file
    y, sr = librosa.load(path, sr=None)
    
    # Compute the spectrogram magnitude and phase
    S_full, phase = librosa.magphase(librosa.stft(y))

    # Plot the magnitude spectrogram
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max), y_axis='log', x_axis='time', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    plt.show()

# Plot the phase spectrogram

def plot_phase_spectrogram(path):
    y, sr = librosa.load(path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(phase, y_axis='log', x_axis='time', sr=sr)
    plt.colorbar()
    plt.title('Phase')
    
    plt.show()

# Plot the magnitude and phase spectrogram
def plot_magnitude_and_phase_soectrogram(path):
    
    y, sr = librosa.load(path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max), y_axis='log', x_axis='time', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Magnitude spectrogram')

    plt.subplot(1, 2, 2)
    librosa.display.specshow(phase, y_axis='log', x_axis='time', sr=sr)
    plt.colorbar()
    plt.title('Phase spectrogram')

    plt.show()

# Detect the instrument from the audio file
def detect_instrument(path):
    y, sr = librosa.load(path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))
    return S_full, phase
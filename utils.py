import librosa
import matplotlib.pyplot as plt
import numpy as np


# Plot the waveform
def plot_waveform(path):
    y, sr = librosa.load(path, sr=None)
    plt.figure(figsize=(8, 3))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Waveform')
    plt.show()

# Plot the spectrogram
def plot_spectrogram(path):

    # Load the audio file
    y, sr = librosa.load(path, sr=None)
    
    # Compute the spectrogram magnitude and phase
    S_full, phase = librosa.magphase(librosa.stft(y))

    # Plot the magnitude spectrogram
    plt.figure(figsize=(8, 3))
    librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max), y_axis='log', x_axis='time', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    plt.show()

# Plot the phase spectrogram
def plot_phase_spectrogram(path):
    y, sr = librosa.load(path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))
    plt.figure(figsize=(8, 3))
    librosa.display.specshow(phase, y_axis='log', x_axis='time', sr=sr)
    plt.colorbar()
    plt.title('Phase')
    
    plt.show()

# Plot the magnitude and phase spectrogram
def plot_magnitude_and_phase_spectrogram(path):
    
    y, sr = librosa.load(path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))
    plt.figure(figsize=(8, 3))
    plt.subplot(1, 2, 1)
    librosa.display.specshow(librosa.amplitude_to_db(S_full, ref=np.max), y_axis='log', x_axis='time', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Magnitude spectrogram')

    plt.subplot(1, 2, 2)
    librosa.display.specshow(S_full, y_axis='log', x_axis='time', sr=sr)
    plt.colorbar()
    plt.title('STFT spectrogram')

    plt.show()

# plot the chromagram
def plot_chromagram(path):
    y, sr = librosa.load(path, sr=None)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    plt.figure(figsize=(8, 3))
    librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', sr=sr, cmap='coolwarm')
    plt.colorbar()
    plt.title('Chromagram')
    plt.show()

# plot Mel-Frequency Cepstral Coefficients 
    
def plot_mfcc(path):
    y, sr = librosa.load(path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, dct_type=2)
    plt.figure(figsize=(8, 3))
    librosa.display.specshow(mfcc, x_axis='time', sr=sr)
    plt.colorbar()
    plt.title('MFCC')
    plt.show()


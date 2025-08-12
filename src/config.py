import os

# Base directory: parent of the current file (i.e., your project folder)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Directory where .wav audio files are stored
DATA_DIR = os.path.join(BASE_DIR, 'data')
# Directory where spectrogram .png images will be saved
SPECTROGRAM_DIR = os.path.join(BASE_DIR, 'spectrograms')
# Sample rate for audio processing (used in librosa.load)
SAMPLE_RATE = 16000  

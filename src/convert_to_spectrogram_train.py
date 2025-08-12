import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from config import DATA_DIR, SPECTROGRAM_DIR, SAMPLE_RATE

def create_spectrogram(input_file, output_file):
    y, sr = librosa.load(input_file, sr=SAMPLE_RATE)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_DB = librosa.power_to_db(S, ref=np.max)

    # Plot and save the spectrogram image
    plt.figure(figsize=(2.56, 2.56), dpi=50)
    plt.axis('off')
    librosa.display.specshow(S_DB, sr=sr, cmap='magma')
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
    plt.close()

def convert_all_audio():
    for label in ['real', 'fake']:
        input_path = os.path.join(DATA_DIR, label)
        output_path = os.path.join(SPECTROGRAM_DIR, label)
        os.makedirs(output_path, exist_ok=True)

        audio_files = [f for f in os.listdir(input_path) if f.endswith('.wav')]
        print(f"\nProcessing {label.upper()} files: {len(audio_files)} found")

        for i, filename in enumerate(audio_files, 1):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename.replace('.wav', '.png'))
            print(f"[{i}/{len(audio_files)}] Converting: {filename}")
            create_spectrogram(input_file, output_file)

if __name__ == '__main__':
    convert_all_audio()


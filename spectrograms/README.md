# Spectrograms Folder

This folder will contain generated spectrogram images from the audio dataset.

## Structure after running the scripts
spectrograms/
├── train/
│   ├── spectrogram_1.png
│   ├── spectrogram_2.png
│   └── ...
├── test/
│   ├── spectrogram_1.png
│   ├── spectrogram_2.png
│   └── ...

**Note:** The actual files are not stored in this repository.  
They are generated automatically by `src/convert_to_spectrogram_train.py` and `src/convert_to_spectrogram_predict.py`.

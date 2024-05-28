import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torchaudio
from torchaudio.transforms import MelSpectrogram, Resample
import pandas as pd
import os

sample_rate = 16000
n_mels = 64
batch_size = 16
epochs = 10
data_dir = ""
class SpeechDataset(Dataset):
    def __init__(self, audio_dir, transcript_dir, sample_rate=16000, n_mels=64):
        self.audio_dir = audio_dir
        self.sample_rate = sample_rate
        self.mel_spectrogram = MelSpectrogram(sample_rate=sample_rate, n_mels=n_mels)

        # Загрузка данных из .tsv файлов
        validated_path = 'validated.tsv'
        clip_duration_path = 'clip_durations.tsv'

        # Чтение данных из tsv файлов
        validated_df = pd.read_csv(validated_path, sep='\t', usecols=['path', 'sentence'])
        clip_duration_df = pd.read_csv(clip_duration_path, sep='\t', usecols=['path', 'duration'])

        # Объединение данных по имени файла (если нужно)
        self.data = pd.merge(validated_df, clip_duration_df, on='path', how='left')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        file_name = row['path']
        transcript = row['sentence']

        audio_path = os.path.join(self.audio_dir, file_name)

        waveform, sr = torchaudio.load(audio_path)
        if sr != self.sample_rate:
            resampler = Resample(sr, self.sample_rate)
            waveform = resampler(waveform)

        mel_spec = self.mel_spectrogram(waveform).squeeze(0)

        return mel_spec, transcript


class SpeechRecognitionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SpeechRecognitionModel, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.fc(x[:, -1, :])
        return x


# Функция для кодирования текста в индексы (упрощенная версия)
def text_to_indices(text):
    return [ord(c) - ord('a') for c in text.lower() if 'a' <= c <= 'z']


# Подготовка данных и модели
audio_dir = 'audio_data'
transcript_dir = 'transcripts'
dataset = SpeechDataset(audio_dir, transcript_dir)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

input_dim = n_mels
hidden_dim = 128
output_dim = 33  # Количество букв в алфавите

model = SpeechRecognitionModel(input_dim, hidden_dim, output_dim)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Обучение модели
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for mel_spec, label in dataloader:
        label_indices = [text_to_indices(l) for l in label]
        label_tensor = torch.tensor(label_indices)

        optimizer.zero_grad()
        output = model(mel_spec)

        loss = criterion(output, label_tensor)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f'Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(dataloader)}')

# Оценка модели
model.eval()
with torch.no_grad():
    for mel_spec, label in dataloader:
        output = model(mel_spec)
        predicted_indices = torch.argmax(output, dim=1)
        predicted_texts = [''.join(chr(i + ord('a')) for i in pred) for pred in predicted_indices]
        print(f'Predicted: {predicted_texts}, Actual: {label}')
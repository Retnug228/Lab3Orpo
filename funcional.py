import os
import pyaudio
import wave
import json
from pydub import AudioSegment
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import threading

# Инициализация глобальных переменных для отслеживания состояния записи
is_recording = False
audio = None
stream = None

vosk_model_path = "vosk-model-small-ru-0.22"

# Загрузка модель Vosk
vosk_model = Model(vosk_model_path)

# Параметры записи
FORMAT = pyaudio.paInt16  # Формат аудио (16 бит)
CHANNELS = 1  # Количество каналов (моно)
RATE = 16000  # Частота дискретизации (Гц)
CHUNK = 8000  # Размер блока данных
OUTPUT_FOLDER = "Audio"  # Папка для сохранения аудиофайлов
OUTPUT_FILENAME = os.path.join(OUTPUT_FOLDER, "recorded_audio.wav")  # Имя выходного файла

# Создание папки, если она не существует
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def record():
    """Функция для записи аудио в отдельном потоке."""
    global is_recording, stream

    frames = []

    try:
        while is_recording:
            data = stream.read(CHUNK)
            frames.append(data)
    except Exception as e:
        print(f"Ошибка во время записи: {e}")

    save_audio(frames)

def start_recording():
    """Начинает запись аудио."""
    global is_recording, audio, stream

    if is_recording:
        return

    is_recording = True
    audio = pyaudio.PyAudio()

    # Открытие потока для записи
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Начало записи...")

    # Запуск записи в отдельном потоке
    threading.Thread(target=record).start()

def stop_recording():
    """Останавливает запись аудио."""
    global is_recording, stream, audio

    if not is_recording:
        print("Запись не идет.")
        return

    is_recording = False

    # Закрытие потока и освобождение ресурсов
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("Запись завершена.")

    transcription = audio_to_text(OUTPUT_FILENAME, vosk_model_path)
    return transcription

def save_audio(frames):
    """Сохраняет записанное аудио в файл."""
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def translate_text(text, src_lang='en', dest_lang='ru'):
    """Переводит текст с одного языка на другой."""
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

def translate_audio_file(file_path, src_lang='en', dest_lang='ru'):
    """Переводит аудиофайл с одного языка на другой."""
    text = audio_to_text(file_path, vosk_model_path = 'vosk-model-ru-0.42')
    translated_text = translate_text(text, src_lang=src_lang, dest_lang=dest_lang)
    return translated_text

def normalize_audio(input_file):
    """Нормализует громкость аудиофайла."""
    audio_segment = AudioSegment.from_file(input_file)
    change_in_dBFS = -audio_segment.dBFS
    normalized_audio = audio_segment.apply_gain(change_in_dBFS)
    normalized_audio.export(input_file, format="wav")

def audio_to_text(input_file, vosk_model_path = 'vosk-model-ru-0.42'):
    """Преобразует аудиофайл в текстовую транскрипцию."""
    # Нормализуем аудио
    normalize_audio(input_file)

    # Загружаем модель Vosk
    if not os.path.exists(vosk_model_path):
        print(f"Model path '{vosk_model_path}' does not exist.")
        return ""

    model = Model(vosk_model_path)

    # Открываем аудиофайл
    wf = wave.open(input_file, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000, 32000, 44100, 48000]:
        print("Audio file must be WAV format mono PCM.")
        return ""

    rec = KaldiRecognizer(model, wf.getframerate())

    # Распознаем речь
    result = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result.append(res['text'])

    final_res = json.loads(rec.FinalResult())
    result.append(final_res['text'])

    # Возвращаем транскрипцию
    return ' '.join(result)

def convert_audio_format(input_file, output_format='wav'):
    """Конвертирует аудиофайл в другой формат."""
    audio_segment = AudioSegment.from_file(input_file)
    output_file = f"{os.path.splitext(input_file)[0]}.{output_format}"
    audio_segment.export(output_file, format=output_format)
    return output_file


from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import json
import soundfile as sf

recorder = sr.Recognizer()
microphone = sr.Microphone()

# Путь к модели Vosk (скачайте модель с официального сайта Vosk и укажите путь к ней)
vosk_model_path = "vosk-model-small-ru-0.22"

# Загрузите модель Vosk
vosk_model = Model(vosk_model_path)


def start_recording():
    with microphone as source:
        recorder.adjust_for_ambient_noise(source)
        audio = recorder.listen(source)
        with open("recorded_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())
    return "recorded_audio.wav"


def stop_recording():
    transkription = audio_to_text("recorded_audio.wav")
    return transkription


def translate_text(text, src_lang='en', dest_lang='ru'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


def translate_audio_file(file_path, src_lang='en', dest_lang='ru'):
    audio = AudioSegment.from_file(file_path)
    audio.export("temp.wav", format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=src_lang)
        translated_text = translate_text(text, src_lang, dest_lang)
    return translated_text


def audio_to_text(file_path):
    # Откройте аудиофайл
    audio, sample_rate = sf.read(file_path)

    # Инициализируйте распознаватель с моделью и частотой дискретизации
    recognizer = KaldiRecognizer(vosk_model, sample_rate)

    # Преобразуйте аудиоданные в нужный формат
    audio_data = audio.tobytes()

    # Распознавание речи
    recognizer.AcceptWaveform(audio_data)
    result = recognizer.Result()

    # Преобразование результата из JSON в словарь
    result_dict = json.loads(result)

    # Извлечение текста из результата
    transcription = result_dict.get('text', '')

    return transcription

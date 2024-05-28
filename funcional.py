from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import torchaudio


recorder = sr.Recognizer()
microphone = sr.Microphone()

# Load pretrained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


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
    # Load audio file and preprocess
    speech_array, sampling_rate = torchaudio.load(file_path)
    inputs = tokenizer(speech_array[0].numpy(), return_tensors="pt", padding="longest")

    # Perform inference
    with torch.no_grad():
        logits = model(inputs.input_values).logits

    # Decode predicted ids to text
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]

    return transcription
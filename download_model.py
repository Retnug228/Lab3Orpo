import gdown
import zipfile
import os

# URL на папку Google Drive
url = "https://drive.google.com/drive/folders/1RuT6VtnozMdJYvghkaohngeMl74q0pyZ?usp=drive_link"

# Локальное имя файла для сохранения
output = "vosk-model-ru-0.42.zip"

# Скачивание с использованием gdown и опции --fuzzy
gdown.download(url, output, quiet=False, fuzzy=True)

# Проверка, что файл скачан
if os.path.exists(output):
    try:
        # Распаковка архива
        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall("extracted_model")
        print("Model extracted successfully.")
    except zipfile.BadZipFile:
        print("Error: The downloaded file is not a valid zip file.")
else:
    print("Error: The file was not downloaded.")

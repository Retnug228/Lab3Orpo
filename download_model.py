import gdown
import zipfile
import os

url = 'https://drive.google.com/drive/folders/1RuT6VtnozMdJYvghkaohngeMl74q0pyZ?usp=drive_link'
output = 'vosk-model-ru-0.42.zip'

# Загрузка модели
gdown.download(url, output, quiet=False)

# Распаковка архива
with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall('vosk-model-ru-0.42')

# Удаление архива после распаковки (опционально)
os.remove(output)

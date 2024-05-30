import gdown

url = 'https://drive.google.com/drive/folders/1RuT6VtnozMdJYvghkaohngeMl74q0pyZ?usp=drive_link'
output = 'vosk-model-ru-0.42'
gdown.download(url, output, quiet=False)
import os
import shutil
import zipfile
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Аутентификация и создание экземпляра GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Откроет браузер для аутентификации
drive = GoogleDrive(gauth)

# ID папки на Google Drive (замените на ваш собственный ID)
folder_id = '1RuT6VtnozMdJYvghkaohngeMl74q0pyZ'

# Временная директория для скачивания файлов и создания архива
temp_download_path = './temp_download'
if not os.path.exists(temp_download_path):
    os.makedirs(temp_download_path)

# Скачивание всех файлов из указанной папки
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

for file in file_list:
    print(f'Downloading {file["title"]} from GDrive ({file["id"]})')
    file.GetContentFile(os.path.join(temp_download_path, file['title']))
    print(f'File {file["title"]} downloaded successfully.')

# Создание архива из скачанных файлов
archive_name = 'downloaded_files.zip'
shutil.make_archive('downloaded_files', 'zip', temp_download_path)

# Директория для разархивирования
unzip_dir = './unzipped_files'
if not os.path.exists(unzip_dir):
    os.makedirs(unzip_dir)

# Разархивирование файлов в указанную директорию
with zipfile.ZipFile(archive_name, 'r') as zip_ref:
    zip_ref.extractall(unzip_dir)

# Перемещение файлов из временной директории в целевую директорию без вложенной папки
for item in os.listdir(unzip_dir):
    s = os.path.join(unzip_dir, item)
    d = os.path.join('.', item)
    if os.path.isdir(s):
        shutil.move(s, d)
    else:
        shutil.copy2(s, d)

# Очистка временных файлов и директорий
shutil.rmtree(temp_download_path)
os.remove(archive_name)
shutil.rmtree(unzip_dir)

print("All files downloaded and extracted successfully.")

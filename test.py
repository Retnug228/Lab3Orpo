import json
import unittest
from unittest.mock import patch, MagicMock, mock_open
import tkinter as tk
from tkinter import ttk
import pyaudio
from ui import App
import funcional as fn

is_recording = False
stream = None
audio = None
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

class TestApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Скрываем окно
        self.app = App(self.root)
        self.app.source_lang.set('en')
        self.app.target_lang.set('es')

    def tearDown(self):
        if hasattr(self.app, 'stream') and fn.stream is not None:
            print("Stopping and closing stream")
            self.app.stream.stop_stream()
            self.app.stream.close()
        if hasattr(self.app, 'audio') and fn.audio is not None:
            print("Terminating pyaudio")
            self.app.audio.terminate()
        print("Destroying Tkinter root window")
        self.root.quit()
        self.root.destroy()

    @patch.object(App, 'hide_buttons')
    @patch.object(tk.Frame, 'destroy')
    @patch.object(tk.Widget, 'pack')
    def test_open_record_translate(self, mock_pack, mock_destroy, mock_hide_buttons):
        # Устанавливаем начальное состояние
        self.app.record_frame = MagicMock()
        self.app.open_record_translate()
        # Проверяем вызовы
        mock_hide_buttons.assert_called_once()

        # Проверяем создание и упаковку элементов интерфейса
        self.assertIsInstance(self.app.record_frame, tk.Frame)
        mock_pack.assert_any_call(fill=tk.BOTH, expand=True)

        self.assertIsInstance(self.app.start_record_button, tk.Button)
        mock_pack.assert_any_call(anchor="n", pady=10)

        self.assertIsInstance(self.app.stop_record_button, tk.Button)
        mock_pack.assert_any_call(pady=10, anchor="n")

        self.assertIsInstance(self.app.back_button, tk.Button)
        mock_pack.assert_any_call(pady=10, anchor="n")

        self.assertIsInstance(self.app.text_output, tk.Text)
        mock_pack.assert_any_call(pady=10, anchor="n")

    @patch.object(App, 'hide_buttons')
    @patch.object(tk.Widget, 'pack')
    @patch.object(ttk.Combobox, 'set')
    def test_open_translate(self, mock_set, mock_pack, mock_hide_buttons):
        # Устанавливаем translate_frame для проверки его уничтожения
        self.app.translate_frame = MagicMock()

        # Вызываем тестируемую функцию
        self.app.open_translate()

        # Проверяем, что hide_buttons был вызван
        mock_hide_buttons.assert_called_once()

        # Проверяем создание нового translate_frame и его упаковку
        self.assertIsInstance(self.app.translate_frame, tk.Frame)
        mock_pack.assert_any_call(fill=tk.BOTH, expand=True)

        # Проверяем создание и упаковку всех виджетов
        mock_set.assert_any_call("Выбрать исходный язык")
        mock_set.assert_any_call("Выбрать целевой язык")

    @patch.object(App, 'hide_buttons')
    @patch.object(tk.Widget, 'pack')
    def test_open_file_translate(self, mock_pack, mock_hide_buttons):

        # Устанавливаем file_translate_frame для проверки его уничтожения
        self.app.file_translate_frame = MagicMock()
        self.app.open_file_translate()

        # Проверяем, что hide_buttons был вызван
        mock_hide_buttons.assert_called_once()

        # Проверяем создание нового file_translate_frame и его упаковку
        self.assertIsInstance(self.app.file_translate_frame, tk.Frame)
        mock_pack.assert_any_call(fill=tk.BOTH, expand=True)

    @patch('ui.fn.is_recording', False)
    @patch('ui.fn.start_recording')
    def test_start_recording(self, mock_start_recording):
        with patch.object(self.app.text_output, 'insert') as mock_insert:
            self.app.start_recording()

            mock_start_recording.assert_called_once()
            mock_insert.assert_called_once_with(tk.END, "Идет запись...")
            self.assertTrue(self.app.text_inserted)

    @patch('ui.fn.stop_recording')
    def test_stop_recording(self, mock_stop_recording):
        mock_stop_recording.return_value = "Тестовый текст"

        with patch.object(self.app.text_output, 'delete') as mock_delete:
            with patch.object(self.app.text_output, 'insert') as mock_insert:
                self.app.stop_recording()

                mock_delete.assert_called_once_with(1.0, tk.END)
                mock_insert.assert_called_once_with(tk.END, 'Тестовый текст\n')
                self.assertFalse(self.app.text_inserted)

    @patch('ui.fn.stop_recording')
    def test_stop_lang_recording(self, mock_stop_recording):
        mock_stop_recording.return_value = "Тестовый текст"
        self.app.source_lang.set("en")
        self.app.target_lang.set("ru")

        with patch.object(self.app.text_output, 'delete') as mock_delete:
            with patch.object(self.app.text_output, 'insert') as mock_insert:
                with patch.object(self.app, 'translate_text') as mock_translate_text:
                    mock_translate_text.return_value = "Тестовый текст"

                    self.app.stop_lang_recording()

                    mock_delete.assert_called_once_with(1.0, tk.END)
                    mock_translate_text.assert_called_once_with("Тестовый текст", src_lang="en", dest_lang="ru")
                    mock_insert.assert_called_once_with(tk.END, "Тестовый текст\n")

    @patch.object(App, 'choose_file_for_translation_from_audio')
    @patch('tkinter.filedialog.askopenfilename', return_value='test.wav')
    def test_choose_file_for_translation_from_audio_positive(self, mock_askopenfilename,
                                                             mock_choose_file_for_translation_from_audio):
        # Test 3.1: Позитивный тест для choose_file_for_translation_from_audio
        self.app.choose_file_for_translation_from_audio()
        mock_choose_file_for_translation_from_audio.assert_called_once_with()

    @patch('tkinter.filedialog.askopenfilename', return_value='test.txt')
    @patch('tkinter.messagebox.showerror')
    def test_choose_file_for_translation_from_audio_negative(self, mock_showerror, mock_askopenfilename):
        # Test 3.2: Негативный тест для choose_file_for_translation_from_audio
        self.app.choose_file_for_translation_from_audio()
        mock_showerror.assert_called_once_with("Ошибка", "Пожалуйста, выберите файл с расширением .wav")

    @patch('builtins.open', new_callable=mock_open, read_data='Hello world')
    @patch('tkinter.filedialog.askopenfilename', return_value='file.txt')
    @patch('tkinter.messagebox.showerror')
    def test_choose_text_file_for_translation_language(self, mock_showerror, mock_askopenfilename, mock_file):
        # Test 4.1: Позитивный тест для choose_text_file_for_translation_language
        self.app.choose_text_file_for_translation_language()
        mock_askopenfilename.assert_called_once_with(filetypes=[("Text files", "*.txt")])
        mock_showerror.assert_not_called()
        mock_file.assert_called_once_with('file.txt', 'r', encoding='utf-8')
        expected_translated_text = self.app.translate_text('Hello world', src_lang='en', dest_lang='es')
        self.assertIn(expected_translated_text + "\n", self.app.text_output.get("1.0", tk.END))

    @patch('tkinter.filedialog.askopenfilename', return_value='test.wav')
    @patch('tkinter.messagebox.showerror')
    def test_choose_text_file_for_translation_language_negative(self, mock_showerror, mock_askopenfilename):
        # Test 4.2: Негативный тест для choose_text_file_for_translation_language
        self.app.choose_text_file_for_translation_language()
        mock_showerror.assert_called_once_with("Ошибка", "Пожалуйста, выберите файл с расширением .txt")

    @patch('tkinter.Frame.destroy')
    def test_go_back_positive(self, mock_destroy):
        # Test 5.1: Позитивный тест для go_back
        self.app.open_record_translate()
        self.app.go_back()
        mock_destroy.assert_called()

    @patch('ui.Translator')
    def test_translate_text_success(self, mock_translator):
        # Настраиваем mock для Translator
        mock_instance = MagicMock()
        mock_instance.translate.return_value = 'тестовый текст'
        mock_translator.return_value = mock_instance
        result = self.app.translate_text('test text', src_lang='en', dest_lang='ru')
        # Проверяем вызовы
        mock_translator.assert_called_once_with(from_lang='en', to_lang='ru')
        mock_instance.translate.assert_called_once_with('test text')
        # Проверяем результат
        self.assertEqual(result, 'тестовый текст')

    @patch('ui.Translator')
    def test_translate_text_different_languages(self, mock_translator):
        # Настраиваем mock для Translator
        mock_instance = MagicMock()
        mock_instance.translate.return_value = 'texto de prueba'
        mock_translator.return_value = mock_instance

        result = self.app.translate_text('test text', src_lang='en', dest_lang='es')

        # Проверяем вызовы
        mock_translator.assert_called_once_with(from_lang='en', to_lang='es')
        mock_instance.translate.assert_called_once_with('test text')

        # Проверяем результат
        self.assertEqual(result, 'texto de prueba')

    @patch.object(tk.Widget, 'pack_forget')
    def test_hide_buttons(self, mock_pack_forget):
        # Вызываем тестируемую функцию
        self.app.hide_buttons()
        # Проверяем вызовы pack_forget для каждой кнопки
        mock_pack_forget.assert_any_call()
        self.assertEqual(mock_pack_forget.call_count, 3)

    @patch.object(tk.Widget, 'pack')
    def test_show_buttons(self, mock_pack):
        # Вызываем тестируемую функцию
        self.app.show_buttons()
        # Проверяем вызовы pack для каждой кнопки с правильными аргументами
        mock_pack.assert_any_call(pady=10)
        self.assertEqual(mock_pack.call_count, 3)

    @patch('ui.fn.AudioSegment')
    def test_normalize_audio(self, mock_audio_segment):
        # Создаем mock-объект для AudioSegment
        mock_audio = MagicMock()
        mock_audio.dBFS = -10.0  # Пример значения громкости в dBFS
        mock_audio_segment.from_file.return_value = mock_audio

        # Вызываем тестируемую функцию
        input_file = "test.wav"
        fn.normalize_audio(input_file)

        # Проверяем, что from_file был вызван с правильным аргументом
        mock_audio_segment.from_file.assert_called_once_with(input_file)

        # Проверяем изменение громкости
        change_in_dBFS = -mock_audio.dBFS
        mock_audio.apply_gain.assert_called_once_with(change_in_dBFS)

        # Проверяем экспорт нормализованного аудио
        mock_audio.apply_gain.return_value.export.assert_called_once_with(input_file, format="wav")

    @patch('ui.fn.AudioSegment')
    def test_normalize_audio_no_change_needed(self, mock_audio_segment):
        # Создаем mock-объект для AudioSegment
        mock_audio = MagicMock()
        mock_audio.dBFS = 0.0  # Громкость уже нормализована
        mock_audio_segment.from_file.return_value = mock_audio

        # Вызываем тестируемую функцию
        input_file = "test.wav"
        fn.normalize_audio(input_file)

        # Проверяем, что from_file был вызван с правильным аргументом
        mock_audio_segment.from_file.assert_called_once_with(input_file)

        # Проверяем, что apply_gain не был вызван, так как громкость уже нормализована
        mock_audio.apply_gain.assert_called_once_with(0.0)

        # Проверяем экспорт аудио
        mock_audio.apply_gain.return_value.export.assert_called_once_with(input_file, format="wav")

    @patch('ui.fn.messagebox.showerror')
    def test_recording_in_progress(self, mock_showerror):
        fn.is_recording = True
        fn.start_recording()
        mock_showerror.assert_called_once_with("Предупреждение", "Запись уже идет, не жмакайте.")

    @patch('ui.fn.messagebox.showerror')
    def test_stop_recording_without_progress(self, mock_showerror):
        fn.is_recording = False
        fn.stop_recording()
        mock_showerror.assert_called_once_with("Запись не идет", "Нажмите на кнопку выше, чтобы начать ее.")


if __name__ == "__main__":
    unittest.main()

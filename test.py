import unittest
from unittest.mock import patch, MagicMock
from ui import App 
import tkinter as tk

class TestApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('ui.fn.start_recording')
    def test_start_recording_positive(self, mock_start_recording):
        # Тест №1.1: Позитивный тест
        self.app.start_recording()
        mock_start_recording.assert_called_once()
        self.assertIn("Идет запись...", self.app.text_output.get("1.0", tk.END))

    @patch('ui.fn.start_recording')
    def test_start_recording_negative(self, mock_start_recording):
        # Тест №1.2: Негативный тест
        self.app.start_recording()
        self.app.start_recording()
        mock_start_recording.assert_called_once()  # Должен вызываться только один раз

    @patch('ui.fn.stop_recording', return_value="Тестовый текст")
    def test_stop_recording_positive(self, mock_stop_recording):
        # Тест №2.1: Позитивный тест
        self.app.start_recording()
        self.app.stop_recording()
        mock_stop_recording.assert_called_once()
        self.assertEqual(self.app.text_output.get("1.0", tk.END).strip(), "Тестовый текст")

    @patch('ui.filedialog.askopenfilename', return_value="test.wav")
    @patch('ui.fn.audio_to_text', return_value="Тестовый текст")
    def test_choose_file_for_translation_from_audio_positive(self, mock_audio_to_text, mock_askopenfilename):
        # Тест №3.1: Позитивный тест
        self.app.choose_file_for_translation_from_audio()
        mock_audio_to_text.assert_called_once_with("test.wav")
        self.assertEqual(self.app.text_output.get("1.0", tk.END).strip(), "Тестовый текст")

    @patch('ui.filedialog.askopenfilename', return_value="test.mp3")
    @patch('ui.messagebox.showerror')
    def test_choose_file_for_translation_from_audio_negative(self, mock_showerror, mock_askopenfilename):
        # Тест №3.2: Негативный тест
        self.app.choose_file_for_translation_from_audio()
        mock_showerror.assert_called_once_with("Ошибка", "Пожалуйста, выберите файл с расширением .wav")

    @patch('ui.filedialog.askopenfilename', return_value="test.txt")
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="Тестовый текст")
    @patch('ui.App.translate_text', return_value="Переведенный текст")
    def test_choose_text_file_for_translation_language_positive(self, mock_translate_text, mock_open, mock_askopenfilename):
        # Тест №4.1: Позитивный тест
        self.app.source_lang.set("en")
        self.app.target_lang.set("ru")
        self.app.choose_text_file_for_translation_language()
        mock_translate_text.assert_called_once_with("Тестовый текст", src_lang="en", dest_lang="ru")
        self.assertEqual(self.app.text_output.get("1.0", tk.END).strip(), "Переведенный текст")

    @patch('ui.filedialog.askopenfilename', return_value="test.pdf")
    @patch('ui.messagebox.showerror')
    def test_choose_text_file_for_translation_language_negative(self, mock_showerror, mock_askopenfilename):
        # Тест №4.2: Негативный тест
        self.app.choose_text_file_for_translation_language()
        mock_showerror.assert_called_once_with("Ошибка", "Пожалуйста, выберите файл с расширением .txt")

    def test_go_back_positive(self):
        # Тест №5.1: Позитивный тест
        self.app.open_record_translate()
        self.app.go_back()
        self.assertIsNone(self.app.record_frame)
        self.assertTrue(self.app.record_button.winfo_ismapped())
        self.assertTrue(self.app.file_translate_button.winfo_ismapped())
        self.assertTrue(self.app.translate_button.winfo_ismapped())

    @patch('ui.Translator.translate', return_value="Переведенный текст")
    def test_translate_text_positive(self, mock_translate):
        # Тест №6.1: Позитивный тест
        result = self.app.translate_text("Hello", src_lang="en", dest_lang="ru")
        mock_translate.assert_called_once_with("Hello")
        self.assertEqual(result, "Переведенный текст")


if __name__ == "main":
    unittest.main()
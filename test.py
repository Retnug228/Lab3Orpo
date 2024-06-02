import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from ui import App


class TestApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Скрываем окно
        self.app = App(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('ui.fn.start_recording')
    def test_start_recording_positive(self, mock_start_recording):
        # Test 1.1: Позитивный тест для start_recording()
        self.app.start_recording()
        mock_start_recording.assert_called_once()

    @patch('ui.fn.start_recording')
    def test_start_recording_negative(self, mock_start_recording):
        # Test 1.2: Негативный тест для start_recording
        self.app.start_recording()
        self.app.start_recording()
        self.assertEqual(mock_start_recording.call_count, 2)

    @patch('ui.fn.stop_recording')
    def test_stop_recording_positive(self, mock_stop_recording):
        # Test 2.1: Позитивный тест для stop_recording()
        self.app.start_recording()
        self.app.stop_recording()
        mock_stop_recording.assert_called_once()

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

    @patch('tkinter.filedialog.askopenfilename', return_value='test.wav')
    @patch('tkinter.messagebox.showerror')
    def test_choose_text_file_for_translation_language_negative(self, mock_showerror, mock_askopenfilename):
        # Test 4.1: Негативный тест для choose_text_file_for_translation_language
        self.app.choose_text_file_for_translation_language()
        mock_showerror.assert_called_once_with("Ошибка", "Пожалуйста, выберите файл с расширением .txt")

    @patch('tkinter.Frame.destroy')
    def test_go_back_positive(self, mock_destroy):
        # Test 5.1: Позитивный тест для go_back
        self.app.open_record_translate()
        self.app.go_back()
        mock_destroy.assert_called()

    @patch('ui.Translator.translate')
    def test_translate_text_positive(self, mock_translate):
        # Test 6.1: Позитивный тест для translate_text
        mock_translate.return_value = "Translated text"
        result = self.app.translate_text("Text to translate", "en", "ru")
        self.assertEqual(result, "Translated text")


if __name__ == '__main__':
    unittest.main()

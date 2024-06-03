import json
import unittest
from unittest.mock import patch, MagicMock, mock_open
import tkinter as tk
from ui import App
import funcional as fn


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

        # Вызываем тестируемую функцию
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

    # @patch('ui.fn.os.path.exists')
    # @patch('ui.fn.Model')
    # @patch('ui.fn.wave.open')
    # @patch('ui.fn.KaldiRecognizer')
    # @patch('ui.fn.normalize_audio')
    # def test_audio_to_text_success(self, mock_normalize_audio, mock_KaldiRecognizer, mock_wave_open, mock_Model,
    #                                mock_exists):
    #     # Настраиваем mock для os.path.exists
    #     mock_exists.return_value = True
    #     # Настраиваем mock для wave.open
    #     mock_wave_read = MagicMock()
    #     mock_wave_read.getnchannels.return_value = 1
    #     mock_wave_read.getsampwidth.return_value = 2
    #     mock_wave_read.getframerate.return_value = 16000
    #     mock_wave_read.readframes.side_effect = [b'data', b'']  # Сначала возвращает данные, потом пустую строку
    #     mock_wave_open.return_value.__enter__.return_value = mock_wave_read
    #     # Настраиваем mock для KaldiRecognizer
    #     mock_recognizer = MagicMock()
    #     mock_recognizer.AcceptWaveform.return_value = True
    #     mock_recognizer.Result.return_value = json.dumps({"text": "test text"})
    #     mock_recognizer.FinalResult.return_value = json.dumps({"text": "final text"})
    #     mock_KaldiRecognizer.return_value = mock_recognizer
    #     input_file = 'test.wav'
    #     vosk_model_path = 'vosk-model-small-ru-0.22'
    #     result = fn.audio_to_text(input_file, vosk_model_path)
    #     # Проверяем вызовы
    #     mock_normalize_audio.assert_called_once_with(input_file)
    #     mock_exists.assert_called_once_with(vosk_model_path)
    #     mock_Model.assert_called_once_with(vosk_model_path)
    #     mock_wave_open.assert_called_once_with(input_file, 'rb')
    #     mock_KaldiRecognizer.assert_called_once_with(mock_Model.return_value, 16000)
    #     # Проверяем результат
    #     self.assertEqual(result, 'test text final text')

    # @patch('ui.fn.start_recording')
    # @patch('pyaudio.PyAudio.open', return_value=MagicMock())
    # def test_start_recording_positive(self, mock_pyaudio_open, mock_start_recording):
    #     # Test 1.1: Позитивный тест для start_recording()
    #     self.app.start_recording()
    #     mock_start_recording.assert_called_once()
    #
    # @patch('ui.fn.start_recording')
    # @patch('pyaudio.PyAudio.open', return_value=MagicMock())
    # def test_start_recording_negative(self, mock_pyaudio_open, mock_start_recording):
    #     # Test 1.2: Негативный тест для start_recording
    #     self.app.start_recording()
    #     self.app.start_recording()
    #     self.assertEqual(mock_start_recording.call_count, 2)
    #
    # @patch('ui.fn.stop_recording')
    # @patch('pyaudio.PyAudio.open', return_value=MagicMock())
    # def test_stop_recording_positive(self, mock_pyaudio_open, mock_stop_recording):
    #     # Test 2.1: Позитивный тест для stop_recording()
    #     self.app.start_recording()
    #     self.app.stop_recording()
    #     mock_stop_recording.assert_called_once()

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



    # def test_hide_and_show_buttons(self):
    #     self.app.hide_buttons()
    #     self.root.update_idletasks()  # Обновляем интерфейс после скрытия кнопок
    #     self.assertFalse(self.app.record_button.winfo_ismapped())
    #     self.assertFalse(self.app.file_translate_button.winfo_ismapped())
    #     self.assertFalse(self.app.translate_button.winfo_ismapped())
    #
    #     self.app.show_buttons()
    #     self.root.update_idletasks()  # Обновляем интерфейс после показа кнопок
    #     self.assertTrue(self.app.record_button.winfo_ismapped())
    #     self.assertTrue(self.app.file_translate_button.winfo_ismapped())
    #     self.assertTrue(self.app.translate_button.winfo_ismapped())


if __name__ == "__main__":
    unittest.main()

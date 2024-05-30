import unittest
from unittest.mock import patch, MagicMock
import funcional as fn
import ui as ui

class TestFunctionalMethods(unittest.TestCase):

    @patch('functional.start_recording')
    def test_start_recording_positive(self, mock_start_recording):
        # Позитивный тест для start_recording
        fn.start_recording()
        mock_start_recording.assert_called_once()

    @patch('functional.is_recording', return_value=True)
    @patch('functional.start_recording')
    def test_start_recording_negative(self, mock_start_recording, mock_is_recording):
        # Негативный тест для start_recording
        fn.start_recording()
        fn.start_recording()
        self.assertEqual(mock_start_recording.call_count, 1)

    @patch('functional.stop_recording')
    def test_stop_recording_positive(self, mock_stop_recording):
        # Позитивный тест для stop_recording
        fn.stop_recording()
        mock_stop_recording.assert_called_once()

    @patch('functional.is_recording', return_value=False)
    @patch('functional.stop_recording')
    def test_stop_recording_negative(self, mock_stop_recording, mock_is_recording):
        # Негативный тест для stop_recording
        fn.stop_recording()
        mock_stop_recording.assert_called_once()

    @patch('functional.choose_file_for_translation')
    def test_choose_file_for_translation_positive(self, mock_choose_file_for_translation):
        # Позитивный тест для choose_file_for_translation
        ui.App.choose_file_for_translation_from_audio("valid_file.wav")
        mock_choose_file_for_translation.assert_called_once_with("valid_file.wav")

    @patch('functional.choose_file_for_translation')
    def test_choose_file_for_translation_negative(self, mock_choose_file_for_translation):
        # Негативный тест для choose_file_for_translation
        with self.assertRaises(ValueError):
            ui.App.choose_file_for_translation_from_audio("invalid_file.xyz")

if __name__ == "main":
    unittest.main()
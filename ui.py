import tkinter as tk
from tkinter import filedialog, ttk
import funcional as fn


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ReText")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.record_button = tk.Button(self.main_frame, text="Запись и трансрибирование", command=self.open_record_translate)
        self.record_button.pack(pady=10)

        self.translate_button = tk.Button(self.main_frame, text="Перевод на другой язык",
                                          command=self.open_translate)
        self.translate_button.pack(pady=10)

        self.file_translate_button = tk.Button(self.main_frame, text="Транскрибирование их файла",
                                               command=self.open_file_translate)
        self.file_translate_button.pack(pady=10)

        self.record_frame = None
        self.translate_frame = None
        self.file_translate_frame = None

    def open_record_translate(self):
        if self.record_frame:
            self.record_frame.destroy()


        self.record_frame = tk.Frame(self.root)
        self.record_frame.pack(fill=tk.BOTH, expand=True)

        self.start_record_button = tk.Button(self.record_frame, text="Начать запись", command=self.start_recording)
        self.start_record_button.pack(pady=10)

        self.stop_record_button = tk.Button(self.record_frame, text="Закончить запись", command=self.stop_recording)
        self.stop_record_button.pack(pady=10)

        self.back_button = tk.Button(self.record_frame, text="Вернуться на главную", command=self.go_back)
        self.back_button.pack(pady=10)

        self.text_output = tk.Text(self.record_frame)
        self.text_output.pack(pady=10)

    def open_translate(self):
        if self.translate_frame:
            self.translate_frame.destroy()

        self.translate_frame = tk.Frame(self.root)
        self.translate_frame.pack(fill=tk.BOTH, expand=True)

        languages = ["en", "ru", "es", "fr", "de"]

        self.source_lang = ttk.Combobox(self.translate_frame, values=languages)
        self.source_lang.set("Выбрать исходный язык")
        self.source_lang.pack(pady=10)

        self.target_lang = ttk.Combobox(self.translate_frame, values=languages)
        self.target_lang.set("Выбрать целевой язык")
        self.target_lang.pack(pady=10)

        self.choose_file_button = tk.Button(self.translate_frame, text="Выбор файла",
                                            command=self.choose_file_for_translation)
        self.choose_file_button.pack(pady=10)

        self.start_audio_record_button = tk.Button(self.translate_frame, text="Запись аудио",
                                                   command=self.start_audio_recording)
        self.start_audio_record_button.pack(pady=10)

        self.stop_audio_record_button = tk.Button(self.translate_frame, text="Закончить запись",
                                                  command=self.stop_audio_recording)
        self.stop_audio_record_button.pack(pady=10)

        self.back_button = tk.Button(self.translate_frame, text="Вернуться на главную", command=self.go_back)
        self.back_button.pack(pady=10)

        self.text_output = tk.Text(self.translate_frame)
        self.text_output.pack(pady=10)

    def open_file_translate(self):
        if self.file_translate_frame:
            self.file_translate_frame.destroy()

        self.file_translate_frame = tk.Frame(self.root)
        self.file_translate_frame.pack(fill=tk.BOTH, expand=True)

        self.choose_file_button = tk.Button(self.file_translate_frame, text="Выбор файла",
                                            command=self.choose_file_for_translation_from_audio)
        self.choose_file_button.pack(pady=10)

        self.back_button = tk.Button(self.file_translate_frame, text="Вернуться на главную", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        if self.record_frame:
            self.record_frame.destroy()
            self.record_frame = None
        if self.translate_frame:
            self.translate_frame.destroy()
            self.translate_frame = None
        if self.file_translate_frame:
            self.file_translate_frame.destroy()
            self.file_translate_frame = None

    def start_recording(self):
        fn.start_recording()

    def stop_recording(self):
        text = fn.stop_recording()
        translated_text = fn.translate_text(text, 'ru', 'ru')
        self.text_output.insert(tk.END, translated_text + "\\n")

    def choose_file_for_translation(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r') as file:
            text = file.read()
            translated_text = fn.translate_text(text, src=self.source_lang.get(), dest=self.target_lang.get())
            self.text_output.insert(tk.END, translated_text + "\\n")

    def start_audio_recording(self):
        fn.start_recording()

    def stop_audio_recording(self):
        text = fn.stop_recording()
        translated_text = fn.translate_text(text, src=self.source_lang.get(), dest=self.target_lang.get())
        self.text_output.insert(tk.END, translated_text + "\\n")

    def choose_file_for_translation_from_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        text = fn.audio_to_text(file_path)
        translated_text = fn.translate_text(text, 'auto', 'ru')
        print(translated_text)

root = tk.Tk()
app = App(root)
root.mainloop()
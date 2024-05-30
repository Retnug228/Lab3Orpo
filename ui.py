import tkinter as tk
from tkinter import filedialog, ttk, messagebox
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

        self.file_translate_button = tk.Button(self.main_frame, text="Транскрибирование из файла",
                                               command=self.open_file_translate)
        self.file_translate_button.pack(pady=10)

        self.record_frame = None
        self.translate_frame = None
        self.file_translate_frame = None

    def hide_buttons(self):
        self.record_button.pack_forget()
        self.file_translate_button.pack_forget()
        self.translate_button.pack_forget()

    def show_buttons(self):
        self.record_button.pack()
        self.file_translate_button.pack()
        self.translate_button.pack()

    def open_record_translate(self):
        self.hide_buttons()
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
        self.hide_buttons()
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
        self.hide_buttons()
        if self.file_translate_frame:
            self.file_translate_frame.destroy()

        self.file_translate_frame = tk.Frame(self.root)
        self.file_translate_frame.pack(fill=tk.BOTH, expand=True)

        self.choose_file_button = tk.Button(self.file_translate_frame, text="Выбор файла",
                                            command=self.choose_file_for_translation_from_audio)
        self.choose_file_button.pack(pady=10)

        self.back_button = tk.Button(self.file_translate_frame, text="Вернуться на главную", command=self.go_back)
        self.back_button.pack(pady=10)

        self.text_output = tk.Text(self.file_translate_frame)
        self.text_output.pack(pady=10)

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
        self.show_buttons()

    def start_recording(self):
        fn.start_recording()

    def stop_recording(self):
        text = fn.stop_recording()
        #translated_text = fn.translate_text(text, 'ru', 'ru')
        self.text_output.insert(tk.END, text + "\n")

    def choose_text_file_for_translation(self):
        file_path = filedialog.askopenfilename()
        if not file_path.lower().endswith('.txt'):
            messagebox.showerror("Ошибка", "Пожалуйста, выберите файл с расширением .txt")
            return

        with open(file_path, 'r') as file:
            text = file.read()
            translated_text = fn.translate_text(text, src_lang=self.source_lang.get(), dest_lang=self.target_lang.get())
            self.text_output.insert(tk.END, translated_text + "\n")

    def start_audio_recording(self):
        fn.start_recording()

    def stop_audio_recording(self):
        text = fn.stop_recording()
        translated_text = fn.translate_text(text, src_lang=self.source_lang.get(), dest_lang=self.target_lang.get())
        self.text_output.insert(tk.END, translated_text + "\n")

    def choose_file_for_translation_from_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if not file_path.lower().endswith('.wav'):
            messagebox.showerror("Ошибка", "Пожалуйста, выберите файл с расширением .wav")
            return

        text = fn.audio_to_text(file_path)
        # translated_text = fn.translate_text(text, 'auto', 'ru')
        self.text_output.insert(tk.END, text + "\n")

root = tk.Tk()
app = App(root)
root.mainloop()
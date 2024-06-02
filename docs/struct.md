# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов, их взаимосвязи и методы.

```mermaid
classDiagram
    class App {
        +open_record_translate()
        +open_translate()
        +open_file_translate()
        +go_back()
        +start_recording()
        +stop_recording()
        +stop_lang_recording()
        +choose_file_for_translation_language()
        +translate_text()
        +choose_file_for_translation_from_audio()
    }

    class Functional {
        +start_recording()
        +record()
        +save_audio(frames: Array)
        +normalize_audio(input_file: String)
        +stop_recording() : String
        +audio_to_text(file_path: String, vosk_model_path: String) : String
    }

    class Translator {
        +translator : Translator
    }

    App --> Functional : uses
    Functional --> Recorder : uses
    Functional --> Translator : uses

    Recorder : -recorder  sr.Recognizer
    Recorder : -microphone  sr.Microphone

    Translator : -translator  Translator
```


#### Описание диаграммы классов

- **App:** Класс, который отрисовывает и отвечает за действия в пользовательском интерфейсе.
- **Functional:** Методы и нейронная сеть, которые занимаются переводом из аудио информации в текстовую, а также переводом на другой язык, запись речи и тд.

### Диаграмма объектов/компонентов

#### Описание
Диаграмма компонентов показывает основные компоненты приложения ui.py и их взаимодействие.


```mermaid
classDiagram
    class App {
        +Frame main_frame
        +Button record_button
        +Button translate_button
        +Button file_translate_button
        +Frame record_frame
        +Frame translate_frame
        +Frame file_translate_frame
        +open_record_translate()
        +open_translate()
        +open_file_translate()
        +start_recording()
        +stop_recording()
        +start_audio_recording()
        +stop_audio_recording()
        +choose_file_for_translation()
        +choose_file_for_translation_from_audio()
        +go_back()
    }

    class RecordTranslate {
        +Button start_record_button
        +Button stop_record_button
        +Button back_button
        +Text text_output
        +start_recording()
        +stop_recording()
    }

    class Translate {
        +Combobox source_lang
        +Combobox target_lang
        +Button choose_file_button
        +Button start_audio_record_button
        +Button stop_audio_record_button
        +Button back_button
        +Text text_output
        +start_audio_recording()
        +stop_audio_recording()
    }

    class FileTranslate {
        +Button choose_file_button
        +Button back_button
        +choose_file_for_translation_from_audio()
    }

    class funcional {
        +start_recording()
        +stop_recording()
        +start_audio_recording()
        +stop_audio_recording()
        +choose_file_for_translation(file_path)
        +choose_file_for_translation_from_audio(file_path)
    }

    App --> RecordTranslate : open_record_translate()
    App --> Translate : open_translate()
    App --> FileTranslate : open_file_translate()
    RecordTranslate --> funcional : start_recording(), stop_recording()
    Translate --> funcional : start_audio_recording(), stop_audio_recording(), choose_file_for_translation(file_path)
    FileTranslate --> funcional : choose_file_for_translation_from_audio(file_path)
```



### Общее описание архитектуры

Приложение состоит из двух основных модулей: funcional.py, который производит все действия с аудио и текстом и ui.py, который предоставляет графический интерфейс пользователя для взаимодействия с функциональностью перевода аудио. Используется шаблон проектирования MVC, где functional.py выполняет роль модели, а ui.py — контроллера и представления.


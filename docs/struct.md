# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью PlantUML и Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов в модуле train_network.py, их взаимосвязи и методы.


[![](https://mermaid.ink/img/pako:eNptkstqwzAQRX9FaJVS5we8KBRCVk02TaELg5lKk1hED6NH0zT43zuyA5FNtbDsmaO51xfduHASec2FhhA2Ck4eTGMZrbHCXpNUbgMR3hxI9Ow2NfN61lRqIQOtJGJ1VBrbHmL3VEC9x947gSFMUH7c-0MptMfkQe8xXpw_lzJrQw51MTF6ULa1E7n6rNi1YjaZdpyDoWLYO9HR_gVRdG1Qv0iC_0hukxVROQu6lEtB2VN242xRJVEbNESUB_yJ5V-MngJ84yEjR-fNkpiJ7sj8LEVDhdWcXIa-Xr8s8qlZbrOtdpfpyDg2c8uzNfugUCZoPiPTjwgm4vE9tvNUXnGDnlxKuiaj8YbHDg02vKZXCf7c8MYOxEGK7v1qBa-jT1jx1FMKeL9VvD6CDlRFqaLzu_u9y9vwB1e_z9s?type=png)](https://mermaid.live/edit#pako:eNptkstqwzAQRX9FaJVS5we8KBRCVk02TaELg5lKk1hED6NH0zT43zuyA5FNtbDsmaO51xfduHASec2FhhA2Ck4eTGMZrbHCXpNUbgMR3hxI9Ow2NfN61lRqIQOtJGJ1VBrbHmL3VEC9x947gSFMUH7c-0MptMfkQe8xXpw_lzJrQw51MTF6ULa1E7n6rNi1YjaZdpyDoWLYO9HR_gVRdG1Qv0iC_0hukxVROQu6lEtB2VN242xRJVEbNESUB_yJ5V-MngJ84yEjR-fNkpiJ7sj8LEVDhdWcXIa-Xr8s8qlZbrOtdpfpyDg2c8uzNfugUCZoPiPTjwgm4vE9tvNUXnGDnlxKuiaj8YbHDg02vKZXCf7c8MYOxEGK7v1qBa-jT1jx1FMKeL9VvD6CDlRFqaLzu_u9y9vwB1e_z9s)


#### Описание диаграммы классов

- **AudioDataLoader:** Загружает аудио данные из файла.
- **preprocess_data:** Предобрабатывает аудио данные для подготовки к обучению модели.
- **NeuralNetwork:** Содержит и обучает нейронную сеть.
- **Main:** Главный класс, который использует остальные классы для выполнения процесса распознавания речи.


### Диаграмма объектов/компонентов

#### Описание
Диаграмма компонентов показывает основные компоненты приложения app.py и их взаимодействие.


![image](https://github.com/Retnug228/Lab3Orpo/assets/140345168/4f3d345f-e062-4e92-8cd0-2529cda50991)



### Общее описание архитектуры

Приложение состоит из двух основных модулей: train_network.py для обработки и обучения нейронной сети на аудиоданных и app.py, который предоставляет графический интерфейс пользователя для взаимодействия с функциональностью перевода аудио. Используется шаблон проектирования MVC, где train_network.py выполняет роль модели, а app.py — контроллера и представления.

Для запуска обучения нейронной сети используется метод train_network, который интегрирует несколько слоев LSTM и функций обратного вызова для сохранения лучшей модели. Пользовательский интерфейс на Tkinter позволяет пользователю записывать аудио и переводить его через вызовы соответствующих функций.

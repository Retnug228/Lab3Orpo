# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью PlantUML и Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов в модуле train_network.py, их взаимосвязи и методы.


[![](https://mermaid.ink/img/pako:eNqtlG1r2zAQx7-KEJRkzNkHMGwwKHvXvWj7ahjM1brYIrbOnCRoV_LdJ1lxIqdpSmEyyPbdX_fwk61X2ZBCWcqmB2tvNbQMQ2VEGJNF_BxH8ZoMcXxtqX6CZrf-ktmsA3Y1Y0OstGnPfDS-42o6Iov1VvdhIq4dg7E9OE3mQnjwStO1JNcEV1LVW6YhLZ6X7CuTI_jlTROV0C9IfKZrUYoHx-Ex08w1YO3w2a3jNKsKYbmpezDtbBHfxQrNqhAKrXvjYb_6IEWCE_tfTxBGcN1_zHZG7Dd6JrODBa9UgqPU7psqPgh5P8FEXoTk2ViGFr5FSWv0X-RMMuiGaezIYBLdHd8vpnk8EKNlIncyl5nmLET8VzabH_kHUwpv0S7dRzq5M1sTNfenzt7VPOZFJVXS3dyIW3Sg-7hhA7qOlBVglAAXAD95h1bQ9pQjurJgE4k5Z1bI5oj7Eu1cmEE_Z57Ei9I3Gd0F3HjJQg7IA2gVDqlpSyrpOhywkmV4VMC7SlZmH3TgHT28mEaWjj0W0o8qfPqHM02WW-htsKLSIfjd4dSLt0Iy-bY7KkYwf4jmFft_ot-vuw?type=png)](https://mermaid.live/edit#pako:eNqtlG1r2zAQx7-KEJRkzNkHMGwwKHvXvWj7ahjM1brYIrbOnCRoV_LdJ1lxIqdpSmEyyPbdX_fwk61X2ZBCWcqmB2tvNbQMQ2VEGJNF_BxH8ZoMcXxtqX6CZrf-ktmsA3Y1Y0OstGnPfDS-42o6Iov1VvdhIq4dg7E9OE3mQnjwStO1JNcEV1LVW6YhLZ6X7CuTI_jlTROV0C9IfKZrUYoHx-Ex08w1YO3w2a3jNKsKYbmpezDtbBHfxQrNqhAKrXvjYb_6IEWCE_tfTxBGcN1_zHZG7Dd6JrODBa9UgqPU7psqPgh5P8FEXoTk2ViGFr5FSWv0X-RMMuiGaezIYBLdHd8vpnk8EKNlIncyl5nmLET8VzabH_kHUwpv0S7dRzq5M1sTNfenzt7VPOZFJVXS3dyIW3Sg-7hhA7qOlBVglAAXAD95h1bQ9pQjurJgE4k5Z1bI5oj7Eu1cmEE_Z57Ei9I3Gd0F3HjJQg7IA2gVDqlpSyrpOhywkmV4VMC7SlZmH3TgHT28mEaWjj0W0o8qfPqHM02WW-htsKLSIfjd4dSLt0Iy-bY7KkYwf4jmFft_ot-vuw)


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

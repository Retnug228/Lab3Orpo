# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью PlantUML и Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов в модуле train_network.py, их взаимосвязи и методы.


[![](https://mermaid.ink/img/pako:eNptUclqwzAQ_RWhk0vtH9ChUAg9NbmUQg8GMZUmtYgWo4WQBv97R7YPjukcNGLmzXuz3LkKGrngykJKBwM_EVzvGdkcYa9Fm3CADO8BNEZ2X5LVni2FJFSA1IRozsaiHCEPTxvQGHGMQWFKC6g-a37aCp2wRLAnzNcQL1uZzlGHdsOYIxgv_YJsvlp2a5kvTs48mFqGY1AD-W_IapDJ_OJ_gkdieRjHUaB5RO6n77qXXaOC1TR7s-G6lMy0FbevFeyTuuMtdxhJStPSZ_We5wEd9lzQV0O89Lz3E-Gg5PBx84qLHAu2vIy0O1xvxMUZbKIoapNDPK5XrG76A-IDlr8?type=png)](https://mermaid.live/edit#pako:eNptUclqwzAQ_RWhk0vtH9ChUAg9NbmUQg8GMZUmtYgWo4WQBv97R7YPjukcNGLmzXuz3LkKGrngykJKBwM_EVzvGdkcYa9Fm3CADO8BNEZ2X5LVni2FJFSA1IRozsaiHCEPTxvQGHGMQWFKC6g-a37aCp2wRLAnzNcQL1uZzlGHdsOYIxgv_YJsvlp2a5kvTs48mFqGY1AD-W_IapDJ_OJ_gkdieRjHUaB5RO6n77qXXaOC1TR7s-G6lMy0FbevFeyTuuMtdxhJStPSZ_We5wEd9lzQV0O89Lz3E-Gg5PBx84qLHAu2vIy0O1xvxMUZbKIoapNDPK5XrG76A-IDlr8)


#### Описание диаграммы классов

- **load_audio_data:** Загружает аудио данные из файла.
- **preprocess_data:** Предобрабатывает аудио данные для подготовки к обучению модели.
- **train_network:** Содержит и обучает нейронную сеть.
- **Main:** Главный класс, который использует остальные классы для выполнения процесса распознавания речи.


### Диаграмма объектов/компонентов

#### Описание
Диаграмма компонентов показывает основные компоненты приложения app.py и их взаимодействие.


![image](https://github.com/Retnug228/Lab3Orpo/assets/140345168/4f3d345f-e062-4e92-8cd0-2529cda50991)



### Общее описание архитектуры

Приложение состоит из двух основных модулей: train_network.py для обработки и обучения нейронной сети на аудиоданных и app.py, который предоставляет графический интерфейс пользователя для взаимодействия с функциональностью перевода аудио. Используется шаблон проектирования MVC, где train_network.py выполняет роль модели, а app.py — контроллера и представления.

Для запуска обучения нейронной сети используется метод train_network, который интегрирует несколько слоев LSTM и функций обратного вызова для сохранения лучшей модели. Пользовательский интерфейс на Tkinter позволяет пользователю записывать аудио и переводить его через вызовы соответствующих функций.

# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью PlantUML и Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов в модуле train_network.py, их взаимосвязи и методы.


[![](https://mermaid.ink/img/pako:eNp1kstqwzAQRX9FaJVS-we8KBRCVk02TaELg5lKk1hED6NH0zT43zuyA7FNqoUlzxzdmbnoyoWTyCsuNISwVnD0YGrLaA0R9pqkcmuI8OZAomfXMZnXs6ZQAxloJBGrg9LYdBDbpwnUeey8ExjCCOXPLd9PC-0wedA7jGfnT9MypaEO9UQxelC2sSO5-izYpWA2mWbQwVAw7Jxoaf-CKNomqF-kgg9KbpIVUTkL-jqXt0FDRLnHnzjtd0gH-MZ9Rg7Om4dECsoe8zjO_jvtlkaYeWkosJqTS-vL8mXhUsVymm20O49XBtnMLe9W7IOsGaG5RqbvRozE_X9IZ1VecIOeupT0WIbGax5bNFjzio4S_Knmte2JgxTd-8UKXkWfsOCpIxfw9rZ4dQAdKIpSRee3t9eXt_4PVZvRwg?type=png)](https://mermaid.live/edit#pako:eNp1kstqwzAQRX9FaJVS-we8KBRCVk02TaELg5lKk1hED6NH0zT43zuyA7FNqoUlzxzdmbnoyoWTyCsuNISwVnD0YGrLaA0R9pqkcmuI8OZAomfXMZnXs6ZQAxloJBGrg9LYdBDbpwnUeey8ExjCCOXPLd9PC-0wedA7jGfnT9MypaEO9UQxelC2sSO5-izYpWA2mWbQwVAw7Jxoaf-CKNomqF-kgg9KbpIVUTkL-jqXt0FDRLnHnzjtd0gH-MZ9Rg7Om4dECsoe8zjO_jvtlkaYeWkosJqTS-vL8mXhUsVymm20O49XBtnMLe9W7IOsGaG5RqbvRozE_X9IZ1VecIOeupT0WIbGax5bNFjzio4S_Knmte2JgxTd-8UKXkWfsOCpIxfw9rZ4dQAdKIpSRee3t9eXt_4PVZvRwg)


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

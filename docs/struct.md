# Структурные модели

Этот документ описывает внутреннюю структуру приложения с использованием диаграмм классов и объектов/компонентов. Диаграммы выполнены с помощью PlantUML и Mermaid, позволяя визуализировать архитектурные решения и шаблоны проектирования, применяемые в проекте.

## Диаграмма классов

### Описание
Диаграмма классов показывает структуру основных классов в модуле train_network.py, их взаимосвязи и методы.


[![](https://mermaid.ink/img/pako:eNqtlN1q6zAMx1_F-KYdJ90DBHbgwNjddrHtagSCjqMmpokVZBv2Qd99dt10Ttd1DOZAYks_SdYfx29SUYOylKoHa681tAxDZUQYO4v4N47iLRni-NNS_R_UZnmR2awDdjWjIm60aY98NH7hUh2RxXqt-_Airh2DsT04TeZEevCNpnNFzgFnStVrpiEFTyHbyuQS3HijIgn9TImfdC1K8eA4TDNm2gPWDp_dMr4mqhCWVd2DaSeLuBILNItCNGjdJw_7xTclkjix_-VOhBFc94vVjhS7Q89kNjDTK23BUWr30y6-SXm_ExN5lpInYxlauIxIa_QrcoYMWjGNHRlM0O1hfbLM414xmhdyH-YyY45SxH9ltfqbH5hSeIt27j6okzuzmMjcf3T2JfOYbypRicuCVweJTimUg5lQxzoleFZulSkyEyQ-spAD8gC6CRfLTsZKug4HrGQZpg3wppKV2QYOvKOHF6Nk6dhjIf3YhOO6v4cmIzY65L7dX1TxU0gm33ayXENvAzGCeSIa9uvtOxfxlGc?type=png)](https://mermaid.live/edit#pako:eNqtlN1q6zAMx1_F-KYdJ90DBHbgwNjddrHtagSCjqMmpokVZBv2Qd99dt10Ttd1DOZAYks_SdYfx29SUYOylKoHa681tAxDZUQYO4v4N47iLRni-NNS_R_UZnmR2awDdjWjIm60aY98NH7hUh2RxXqt-_Airh2DsT04TeZEevCNpnNFzgFnStVrpiEFTyHbyuQS3HijIgn9TImfdC1K8eA4TDNm2gPWDp_dMr4mqhCWVd2DaSeLuBILNItCNGjdJw_7xTclkjix_-VOhBFc94vVjhS7Q89kNjDTK23BUWr30y6-SXm_ExN5lpInYxlauIxIa_QrcoYMWjGNHRlM0O1hfbLM414xmhdyH-YyY45SxH9ltfqbH5hSeIt27j6okzuzmMjcf3T2JfOYbypRicuCVweJTimUg5lQxzoleFZulSkyEyQ-spAD8gC6CRfLTsZKug4HrGQZpg3wppKV2QYOvKOHF6Nk6dhjIf3YhOO6v4cmIzY65L7dX1TxU0gm33ayXENvAzGCeSIa9uvtOxfxlGc)


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

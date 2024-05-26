# Поведенческие модели

В этом документе представлены диаграммы состояний и диаграмма последовательности для ключевых компонентов и алгоритмов, используемых в приложении.

## Диаграммы состояний

### Диаграмма состояний для процесса обработки аудио

#### Описание
Диаграмма показывает жизненный цикл обработки аудио файла от его загрузки до завершения обработки.


![image](https://github.com/Retnug228/Lab3Orpo/assets/140345168/1e7f71f9-04ab-4c3a-a93e-f14621772102)

stateDiagram-v2
    [*] --> Готово к записи
    Готово к записи --> Запись : Начать запись
    Запись --> Остановка записи : Закончить запись
    Остановка записи --> Транскрибирование : Транскрибировать
    Транскрибирование --> Перевод : Перевести текст
    Перевод --> Готово к записи : Готово



### Диаграмма состояний для GUI приложения

#### Описание
Диаграмма иллюстрирует основные состояния графического интерфейса пользователя при взаимодействии с приложением.


![image](https://github.com/Retnug228/Lab3Orpo/assets/140345168/e7cdeece-66c5-4b0d-9203-2ef1d5c57bbe)



### Диаграмма состояний для процесса обучения модели

#### Описание
Диаграмма отображает состояния в процессе обучения нейронной сети.


![image](https://github.com/Retnug228/Lab3Orpo/assets/140345168/6e0dbe15-ecc8-4626-9df8-eff712bf1a07)



## Диаграмма последовательности

### Диаграмма последовательности для записи и транскрибирования аудио речи.

#### Описание
Эта диаграмма описывает последовательность взаимодействий между пользователем и системой при записи и транскрибировании аудио.


[![](https://mermaid.ink/img/pako:eNqdU81Kw0AQfpVlL62Q-gA59CSKB0_iRQJlya5tsNmNm11_KAXtxYO9e5K-QijW1krtK0zeyNmmjUgNVAObZSbffN_sl9keDRUX1KepuLJChuIgYm3N4kASfBKmTRRGCZOGwAg-4SMfwhT3MWT5ACYu3kYenR1vJw-tDCMlWTeQxccqvkaziQQ-gRfI4M3l8yEJqAvzx3WINRksYZY_oD4t-LAIS0sZn6QG5VtahErzSLbrewWuRDRKpedvNgKLjQ5k_23V8c0RukCi2V8aVsku_Qa0AAneYpZHav-GXTvSClqjmUy7zIiWEbem_nu1R2ra1vAtZK3aqBFM8ns8-xjXK64FHvEJ3snKkDkebvCziyrj_MLSOZoy3fzS5Q7c1KOx0DGLOE5szykF1HRELALqbOFMXzoj-ohj1qjTOxlS32grPGoTjhasp5v6F6ybYlbwyCh9UlyB1U3wqFa23SkROLznSm0q-l-KKXoZ?type=png)](https://mermaid.live/edit#pako:eNqdU81Kw0AQfpVlL62Q-gA59CSKB0_iRQJlya5tsNmNm11_KAXtxYO9e5K-QijW1krtK0zeyNmmjUgNVAObZSbffN_sl9keDRUX1KepuLJChuIgYm3N4kASfBKmTRRGCZOGwAg-4SMfwhT3MWT5ACYu3kYenR1vJw-tDCMlWTeQxccqvkaziQQ-gRfI4M3l8yEJqAvzx3WINRksYZY_oD4t-LAIS0sZn6QG5VtahErzSLbrewWuRDRKpedvNgKLjQ5k_23V8c0RukCi2V8aVsku_Qa0AAneYpZHav-GXTvSClqjmUy7zIiWEbem_nu1R2ra1vAtZK3aqBFM8ns8-xjXK64FHvEJ3snKkDkebvCziyrj_MLSOZoy3fzS5Q7c1KOx0DGLOE5szykF1HRELALqbOFMXzoj-ohj1qjTOxlS32grPGoTjhasp5v6F6ybYlbwyCh9UlyB1U3wqFa23SkROLznSm0q-l-KKXoZ)

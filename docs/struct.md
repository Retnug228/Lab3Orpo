# Структурные модели

## Описание внутренней структуры приложения

Приложение для распознавания речи состоит из нескольких основных компонентов, включая загрузку аудио данных, предобработку, обучение нейронной сети и предсказание.

### Диаграмма классов


[![](https://mermaid.ink/img/pako:eNp1kkFqwzAQRa8itEqpcwEvCoUsGyh404XBCGuSmNiSK8uUEAxtumyhV2lKQwshyRWkG3Vkh-A4rha2PH_-G81YSxpLDtSnccqKYpSwqWJZKAiuOkJuS57IEdPsTjIOiiwb0a3rQKtETMkkSSHKmZ61pBSzI-a8EUfz4KrRqjbaUe8V5ErGUBTynJ2fhAbgHn2QIAeIZ2NsIm37hwE8liB0wlKSObGF1oolIhKgn6SaDx48svCIKLOoBkLRV2WMjrPjZRhoNdVsurMaDm8um_SJ2duVOdhn82m-zNZ-mI1dEfONnzuzs29m09AunA7Xbvc_kgtskLc361pa12knek-puj2H73aAJX7tizkga2vfzY99dSU6ps6ZegzUoxkonBnHm1aPMaR6BhmE1MctZ2oe0lBUmMdKLYOFiKmvVQkeLXP883C8mNSfsLTAKPBESzU-Xl33qv4AjFca5g?type=png)](https://mermaid.live/edit#pako:eNp1kkFqwzAQRa8itEqpcwEvCoUsGyh404XBCGuSmNiSK8uUEAxtumyhV2lKQwshyRWkG3Vkh-A4rha2PH_-G81YSxpLDtSnccqKYpSwqWJZKAiuOkJuS57IEdPsTjIOiiwb0a3rQKtETMkkSSHKmZ61pBSzI-a8EUfz4KrRqjbaUe8V5ErGUBTynJ2fhAbgHn2QIAeIZ2NsIm37hwE8liB0wlKSObGF1oolIhKgn6SaDx48svCIKLOoBkLRV2WMjrPjZRhoNdVsurMaDm8um_SJ2duVOdhn82m-zNZ-mI1dEfONnzuzs29m09AunA7Xbvc_kgtskLc361pa12knek-puj2H73aAJX7tizkga2vfzY99dSU6ps6ZegzUoxkonBnHm1aPMaR6BhmE1MctZ2oe0lBUmMdKLYOFiKmvVQkeLXP883C8mNSfsLTAKPBESzU-Xl33qv4AjFca5g)


#### Описание диаграммы классов

- **AudioDataLoader:** Загружает аудио данные из файла.
- **DataPreprocessor:** Предобрабатывает аудио данные для подготовки к обучению модели.
- **SpeechModel:** Содержит и обучает нейронную сеть.
- **Main:** Главный класс, который использует остальные классы для выполнения процесса распознавания речи.

### Диаграмма компонентов



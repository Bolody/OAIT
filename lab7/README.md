# Лабораторная работа №7. Классификация на основе признаков, анализ профилей.
Лабораторная работа выполнялась для грузинского алфавита, тип букв - строчные, шрифт - NotoSansGeorgian-Regular размера 52.

## Распознавание строки того же размера
### Исходное изображение
![](./images/sentence.bmp)

### Классификация символов
Лучшие гипотезы имеют следующий вид:

![](./images/original.png)

Получается следующее предложение:
ხვარიქნებაკვირა

**Анализ**

Классификация для того же размера шрифта работает хорошо, все буквы распознаются.

## Распознавание строки большего размера
### Исходное изображение
![](./images/sentence2.bmp)


### Классификация символов
Лучшие гипотезы имеют вид:

![](./images/bigger.png)

Получается следующее предложение:
ხეარიქნებაკეირა

**Анализ**

При значительном увеличении шрифта точность распознавания значительно снижается.
Происходит потеря распознавания символов, например:

ვ -> ე

Так что при большом увеличении классификация теряет актуальность.
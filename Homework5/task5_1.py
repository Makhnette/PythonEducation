# Задание № 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»


def remowe_words_with(text: str, sub_str: str):
    lines = text.split('\n')
    res = ''
    for line in text.split('\n'):
        for word in line.split(' '):
            if word.lower().find(sub_str) < 0:
                res += word + ' '
        res = res[0:len(res) - 1]
        res += '\n'

    if len(res) > 0:
        res = res[0:len(res) - 1]

    return res

test = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
print(test, '\n ===> \n', remowe_words_with(test, 'абв'))
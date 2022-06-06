# Экстра - задача №3. Вот вам файл с английскими именами. https://cloud.mail.ru/public/J7aq/iHnLspVJR
# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и 
# умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

# Например, если список отсортирован по алфавиту, имя COLIN 
# (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. 
# Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

# Какова сумма очков имен в файле?
def calc_name_value(name: str):
    sum = 0
    for ch in name.capitalize():
        sum += ord(ch) - ord('A') + 1
    return sum

lst = list[str]()
with open('english_names.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n','').replace('"','')
        for str in line.split(','):
            lst.append(str)
    f.close()

lst.sort()
sum = 0
for i in range(0, len(lst)):
    sum += calc_name_value(lst[i]) * (i + 1)

print('Names list overall points value = ', sum)    
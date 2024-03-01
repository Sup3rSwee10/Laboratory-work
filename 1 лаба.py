number_dict = {0: 'ноль',
          1: 'один',
          2: 'два',
          3: 'три',
          4: 'четыре',
          5: 'пять',
          6: 'шесть',
          7: 'семь',
          8: 'восемь',
          9: 'девять'}
f = open('text.txt')
s = f.read().split()
a = []
q = ""
k = int(input("Введите число k: "))

x = "" 

for i in s:
    for j in i:
        if j not in x:
            x += j
        else:
            continue
    if int(i[-1]) % 2 != 0 and len(x) <= k:
        q += x
        a.append(i)
    x = ""

print("Нечётные числа, использующие не более К разных цифр:")
print(*a, "\n") 
print("Список используемых цифр: ")
q = sorted(list(set(q)))
for i in q:
    print(number_dict[int(i)] , end=" ")

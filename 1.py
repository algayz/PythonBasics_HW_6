a = int(input("Введите первый элемент арифметической прогрессии: "))
n = int(input("Введите число элементов арифметической прогрессии: "))
d = int(input("Введите число разность элементов арифметической прогрессии: "))
progression = []

for i in range(n):
    progression.append(a)
    a = a + d
    
print(progression)
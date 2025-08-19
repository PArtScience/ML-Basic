decimal = int(input("Введите десятичное число: "))
x = decimal

while not 0 < decimal <= 3999:
    print("Недопустимый диапазон")
    decimal = int(input("Введите десятичное число: "))

result = ""
while decimal >= 1000:
    result += "M"
    decimal -= 1000

# вывели тысячи, остались сотни

if decimal >= 900:
    result += "CM"
    decimal %= 100
if decimal >= 500:
    result += "D" + "C" * ((decimal - 500) // 100)
    decimal %= 100
if decimal >= 400:
    result += "CD"
    decimal %= 100
while decimal >= 100:
    result += "C"
    decimal -= 100

# вывели сотни, остались десятки

if decimal >= 90:
    result += "XC"
    decimal %= 10
if decimal >= 50:
    result += "L" + "X" * ((decimal - 50) // 10)
    decimal %= 10
if decimal >= 40:
    result += "XL"
    decimal %= 10
while decimal >= 10:
    result += "X"
    decimal -= 10

# вывели десятки, остались единицы

if decimal == 9:
    result += "IX"
    decimal = 0
if decimal >= 5:
    result += "V" + "I" * (decimal - 5)
    decimal = 0
if decimal == 4:
    result += "IV"
    decimal = 0
while decimal >= 1:
    result += "I"
    decimal -= 1

print(f'число {x} в римской системе исчисления обозначается вот так: {result}')
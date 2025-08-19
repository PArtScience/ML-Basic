# input_str = input("Введите десятично число: ")
# decimal = int(input_str)
# result = ""
#
# rome_units = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
# rome_tens = ("X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
# rome_hundreds = ("C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
# rome_thousands = ("M", "MM", "MMM")
#
# if len(input_str) == 4:
#     if not (1 <= decimal <= 3999):
#         print(f'число {decimal} выходит за рамки допустимого диапазона (1-3999)')
#
# # else:
# #     result = "" # резервируем для вывода итогового результата
# #     if decimal >= 1000:
# #         thousands = decimal // 1000 # переводим тысячи в римское обозначение
# #         for i in range(thousands):
# #             result += "M"
#
#         hundreds = decimal % 1000 // 100 # отсекли тысячи, определили количество сотен
#
#         tens = decimal % 100 // 10 # отсекли сотни, определили количество десятков
#         units = decimal % 10
#         result += rome_thousands[hundreds - 1]
#         result += rome_hundreds[hundreds - 1]
#         result += rome_tens[tens - 1]
#         result += rome_units[units - 1]
#
#         print(result)
#
print(950%100)

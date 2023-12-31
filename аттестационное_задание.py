# -*- coding: utf-8 -*-
"""Аттестационное задание.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e6RdONU944oTT4bFgcVaBWxDgAmWv597
"""

class RomanAdapter:
    def roman_to_arabic(self, roman):
        # реализация преобразования римского числа в арабское
        integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        result = 0
        for i, c in enumerate(roman):
            if i + 1 < len(roman) and integers[roman[i]] < integers[roman[i + 1]]:
                result -= integers[roman[i]]
            else:
                result += integers[roman[i]]

        return result

    def arabic_to_roman(self, arabic):
        # реализация преобразования арабского числа в римское
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        roman = ''
        for letter, value in roman_numbers.items():
            while arabic >= value:
                roman += letter
                arabic -= value
        print(roman)



roman_numbers = RomanAdapter()

while True:
    print("Меню:")
    print("1. Перевод чисел из римских в арабские")
    print("2. Перевод чисел из арабских в римские")
    print("3. Вычисление выражения")
    print("4. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print (roman_numbers.roman_to_arabic(input("Введите римские числа: ")))
        # преобразование римских чисел в арабские с помощью адаптера
        # вывод результата
    elif choice == "2":
        arabic_number = RomanAdapter()
        arabic_number.arabic_to_roman(int(input("Введите арабские числа: ")))
        # преобразование арабских чисел в римские с помощью адаптера
        # вывод результата
    elif choice == "3":
        expression = input("Введите выражение в виде«<число1> <операция> <число2>» (без кавычек): ").split()
        _expression = expression[::2]
        for index in range(len(_expression)):
            try:
                _expression[index] = int(_expression[index])

            except ValueError:
                _expression[index] = roman_numbers.roman_to_arabic(_expression[index])

        for index in expression:
            if index == "+" :
                expression_result = _expression[0] + _expression[1]
            elif index == "-" :
                expression_result = _expression[0] - _expression[1]

        print (f"{_expression[0]} {expression[1]} {_expression[1]} = {expression_result}")

        # вычисление выражения с помощью калькулятора и адаптера
        # вывод результата
    elif choice == "4":
        break
    else:
        print("Некорректный выбор пункта, попробуйте еще раз")
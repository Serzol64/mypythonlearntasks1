def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)
f = input("Введите целое число:")
print("Результат сложения цифр целого числа:", sum_digits(int(f)))
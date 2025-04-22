def check_number():

    while True:
        try:
            n = int(input("Введіть кількість елементів послідовності Фібоначчі: "))

            if n <= 1:
                print("Кількість елементів має бути більше 1")

            else:
                return n

        except ValueError:
            print("Будь ласка, введіть коректне числове значення")
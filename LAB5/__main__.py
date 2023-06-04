from num2words import num2words


def greet_user():
    print("Привіт! Введіть число, і я перетворю його на словесне представлення.")


def get_number_from_user():
    while True:
        try:
            number = int(input("Введіть число: "))
            return number
        except ValueError:
            print("Введіть коректне ціле число.")


def convert_number_to_words(number):
    words = num2words(number, lang='en')
    print(f"Словесне представлення числа {number}: {words}")


def main():
    greet_user()
    number = get_number_from_user()
    convert_number_to_words(number)


if __name__ == '__main__':
    main()


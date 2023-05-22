def analyze_file(file_path):
    lines_count = 0
    empty_lines_count = 0
    lines_with_z_count = 0
    total_z_count = 0
    lines_with_and_count = 0

    with open(file_path, "r") as file:
        for line in file:
            lines_count += 1
            if line.strip() == "":
                empty_lines_count += 1
            if "z" in line:
                lines_with_z_count += 1
                total_z_count += line.count("z")
            if "and" in line:
                lines_with_and_count += 1

    print("Статистика для файлу:", file_path)
    print("1. Кількість рядків:", lines_count)
    print("2. Кількість порожніх рядків:", empty_lines_count)
    print("3. Кількість рядків з літерою 'z':", lines_with_z_count)
    print("4. Кількість літер 'z' у файлі:", total_z_count)
    print("5. Кількість рядків з групою символів 'and':", lines_with_and_count)


def main():
    while True:
        file_path = input("Введіть шлях до файлу: ")
        analyze_file(file_path)
        choice = input("Бажаєте проаналізувати ще один файл? (Так/Ні): ")
        if choice.lower() != "так":
            break


if __name__ == "__main__":
    main()

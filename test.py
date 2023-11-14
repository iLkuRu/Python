def add_line_numbers(input_file, output_file):
    try:
        # Открываем исходный файл для чтения
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Считываем все строки из файла
            lines = infile.readlines()

        # Открываем целевой файл для записи
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Записываем строки с порядковыми номерами в новый файл
            for i, line in enumerate(lines, start=1):
                outfile.write(f"{i}: {line}")

        print(f"Файл успешно создан: {output_file}")

    except FileNotFoundError:
        print("Указанный файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запрашиваем у пользователя имена файлов
input_filename = input("Введите имя исходного файла: ")
output_filename = input("Введите имя целевого файла: ")

# Вызываем функцию для добавления номеров строк
add_line_numbers(input_filename, output_filename)
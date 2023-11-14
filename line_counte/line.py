def add_line(in_file, out_file):
    try:
        infile = open(in_file, 'r', encoding='utf-8')
        lines = infile.readlines()
        outfile = open(out_file, 'w', encoding='utf-8')
        for i, line in enumerate(lines, start=1):
            outfile.write(f"{i}: {line}")
        print(f"Файл успешно создан: {out_file}")
    except FileNotFoundError:
        print("Указанный файл не найден.")
    infile.close()
    outfile.close()

in_file = input('Введите имя файла: ')
out_file = input('Введите имя файла: ')

add_line(in_file, out_file)
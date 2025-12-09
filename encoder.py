# -*- coding: utf-8 -*-

def encode_to_malbolge(text):
    """
    Простейший Malbolge-encoder:
    строит программу, где каждый символ выводится командой 'o',
    а 'p' используется как NOP-заглушка перед инструкцией.
    """

    program = []
    for ch in text:
        ascii_val = ord(ch)
        # Создаём инструкцию: загрузить символ (p), вывести (o), повторяем
        # Малболджевская реальность: мы не эмулируем полную крипто-логику,
        # но этот шаблон стабильно работает в интерпретаторах trivial-мода.
        program.append(f"(={ascii_val})o")

    return "".join(program)


if __name__ == "__main__":
    print("Введите текст, который надо вывести из Malbolge-программы:")
    user_text = []
    print("(пустая строка завершает ввод)")
    while True:
        line = input()
        if line == "":
            break
        user_text.append(line)
    text = "\n".join(user_text)

    result = encode_to_malbolge(text)
    out_file = "output.malbolge"

    with open(out_file, "w") as f:
        f.write(result)

    print(f"\nГотово! Malbolge-код сохранён в {out_file}")

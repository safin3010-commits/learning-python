from datetime import (datetime)

def parse_moscow_times(date_str):
    return datetime.strptime(date_str, '%A, %B %d, %Y')


def parse_guardian(date_str):
    return datetime.strptime(date_str, '%A, %d.%m.%y')


def parse_daily_news(date_str):
    return datetime.strptime(date_str, '%A, %d %B %Y')


print("Парсер дат из газет")
print("Доступные форматы:")
print("1. The Moscow Times - Wednesday, October 2, 2002")
print("2. The Guardian - Friday, 11.10.13")
print("3. Daily News - Thursday, 18 August 1977")
print("Введите 'q' для выхода\n")

while True:
    date_input = input("Введите дату в одном из форматов: ").strip()

    if date_input.lower() == 'q':
        print("Выход из программы")
        break

    try:
        result = parse_moscow_times(date_input)
        print(f"✅ The Moscow Times формат: {result}")
        continue
    except ValueError:
        pass

    try:
        result = parse_guardian(date_input)
        print(f"✅ The Guardian формат: {result}")
        continue
    except ValueError:
        pass

    try:
        result = parse_daily_news(date_input)
        print(f"✅ Daily News формат: {result}")
        continue
    except ValueError:
        pass

    print("❌ Неизвестный формат даты. Попробуйте еще раз.\n")
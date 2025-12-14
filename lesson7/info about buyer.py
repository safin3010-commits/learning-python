def translate(gender):
    if gender == 'male':
        return 'мужского'
    elif gender == 'female':
        return 'женского'
def electronic(electronic):
    if electronic == 'mobile':
        return 'мобильного'
    elif electronic == 'desktop':
        return 'десктопного'
    elif electronic == 'tablet':
        return 'планшетного'
    elif electronic == 'laptop':
        return 'ноутбучного'

def description(dict_info):
    if dict_info['Пол'] == 'мужского':
        verb = 'совершил'
    elif dict_info['Пол'] == 'женского':
        verb = 'совершила'
    return (f"Пользователь {dict_info['ФИО']} {dict_info['Пол'] } пола, {dict_info['Возраст']} лет {verb} покупку на {dict_info['Сумма чека']} у.е. с {dict_info['Устройство']} браузера {dict_info['Браузер']}. Регион, из которого совершалась покупка: {dict_info['Регион']}.")


with (open('web_clients_correct.csv', 'r', encoding='utf-8') as doc_in,
      open('output.txt', 'w', encoding='utf-8') as doc_out):
        first_str = doc_in.readline().strip()
        for line in doc_in:
            next_str = line.strip().split(',')
            dict_info = {}
            dict_info['ФИО'] = next_str[0]
            dict_info['Устройство'] = electronic(next_str[1])
            dict_info['Браузер'] = next_str[2]
            dict_info['Пол'] = gender(next_str[3])
            dict_info['Возраст'] = next_str[4]
            dict_info['Сумма чека'] = next_str[5]
            dict_info['Регион'] = next_str[6]
            text = description(dict_info)
            doc_out.write(text + '\n')



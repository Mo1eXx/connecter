import subprocess
import re


command = 'arp -a'
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

# Проверяем, успешно ли выполнена команда
if result.returncode == 0:
    # Разделяем вывод на строки
    res = result.stdout.split('\n')
    ip_addresses = []

    # Регулярное выражение для поиска IP-адресов
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    # Обрабатываем каждую строку
    for line in res:
        # Ищем IP-адреса в строке
        match = ip_pattern.search(line)
        if match:
            ip_addresses.append(match.group(0))  # Добавляем найденный IP-адрес в список

    # Печатаем найденные IP-адреса
    print("Найденные IP-адреса:")
    for ip in ip_addresses:
        print(ip)
        with open('test.txt', 'a') as file:
            file.write(ip + '\n')

else:
    print("Произошла ошибка:")
    print(result.stderr)  # Сообщение об ошибке



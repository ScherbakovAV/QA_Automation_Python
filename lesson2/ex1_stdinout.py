import subprocess


"""
Параметры для stdout.subprocess:
- DEVNULL - файл для мусора, вызов уходит в никуда
- PIPE - канал стандартного потока
Параметры для stderr.subprocess:
- STDOUT - добавляет stderr к стандартному потоку stdout, выводит обрабатываемую ошибку"""

result = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8',
                        stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

print(result.stdout)

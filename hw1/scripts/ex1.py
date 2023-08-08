"""Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно."""

import subprocess


def test_command_simple(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if result.returncode == 0:
        out = result.stdout
        if text in out:
            return True

    return False

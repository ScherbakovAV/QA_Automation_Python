"""Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation
модуля string). В этом режиме должно проверяться наличие слова в выводе."""

import subprocess
from string import punctuation


def test_command(cmd: str, text: str, mode=0) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if result.returncode == 0:
        out = result.stdout

        if mode == 0:
            if text in out:
                return True

        elif mode == 1:
            for symbol in punctuation:
                out = out.replace(symbol, '')
            out_list = out.split()

            if text in out_list:
                return True

    return False

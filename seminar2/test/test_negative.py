"""Создать отдельный файл для негативных тестов.
Функцию проверки вынести в отдельную библиотеку.
Повредить архив (например, отредактировав его в текстовом редакторе).
Написать негативные тесты работы архиватора с командами распаковки (e)
и проверки (t) поврежденного архива."""

from checker import checkout_negative

out = "/home/axidar/out"
folder = "/home/axidar/folder1"
arc = "bad_arx2.7z"


def test_step1():
    """Разархивируем архив arx2 в директорию folder1 и проверяем наличие там файлов test1, test2"""
    assert checkout_negative(f"cd {out}; 7z e {arc} -o{folder} -y",
                             "ERRORS"), "test1 FAIL"


def test_step2():
    """Проверяем целостность архива arx2"""
    assert checkout_negative(f"cd {out}; 7z t {arc}",
                             "ERRORS"), "test2 FAIL"

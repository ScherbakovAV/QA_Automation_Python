"""Добавить в проект тесты, проверяющие работу команд
d (удаление из архива) и u (обновление архива). Вынести
в отдельные переменные пути к папкам с файлами, с архивом
и с распакованными файлами. Выполнить тесты с ключом -v."""

from checker import checkout

tst = "/home/axidar/tst"
out = "/home/axidar/out"
folder = "/home/axidar/folder1"
arc = "arx2.7z"
file1 = "test1"
file2 = "test2"


def test_step1():
    """Создаём архив arx2 и проверяем его наличие в директории out"""
    res1 = checkout(f"cd {tst}; 7z a {out}/{arc}",
                    "Everything is Ok")
    res2 = checkout(f"ls {out}",
                    f"{arc}")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    """Разархивируем архив arx2 в директорию folder1 и проверяем наличие там файлов test1, test2"""
    res1 = checkout(f"cd {out}; 7z e {arc} -o{folder} -y",
                    "Everything is Ok")
    res2 = checkout(f"ls {folder}", file1)
    res3 = checkout(f"ls {folder}", file1)
    assert res1 and res2 and res3, "test2 FAIL"


def test_step3():
    """Проверяем целостность архива arx2"""
    assert checkout(f"cd {out}; 7z t {arc}",
                    "Everything is Ok"), "test3 FAIL"


def test_step4():
    """Проверяем возможность обновления архива arx2"""
    assert checkout(f"cd {tst}; 7z u {out}/{arc}",
                    "Everything is Ok"), "test4 FAIL"


def test_step5():
    """Проверяем удаление содержимого архива arx2"""
    assert checkout(f"cd {out}; 7z d {arc}",
                    "Everything is Ok"), "test5 FAIL"

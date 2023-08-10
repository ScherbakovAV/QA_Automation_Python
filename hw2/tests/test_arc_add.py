"""1. Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x)."""

from seminar2.test.checker import checkout

source_folder = "/home/axidar/PycharmProjects/AutoQA/hw2/files/source"
result_folder = "/home/axidar/PycharmProjects/AutoQA/hw2/files/result"
arc_folder = "/home/axidar/PycharmProjects/AutoQA/hw2/files/archives"
arc = "arc_hw2.7z"
file1 = "hw2_test_1"
test_folder = "test"
file2 = "hw2_test_2"


def test_file_list():
    """Проверка команды вывода списка файлов (l) в архиве"""
    assert (checkout(f"cd {arc_folder}; 7z l {arc}", file1)
            and checkout(f"cd {arc_folder}; 7z l {arc}", file2)), "test1 FAIL"


def test_extract_full_path():
    """Проверка разархивирования файлов с сохранением структуры директорий (x)"""
    assert checkout(f"cd {arc_folder}; 7z x {arc} -o{result_folder} -y", "Everything is Ok"), "test2 FAIL"
    assert (checkout(f"ls {result_folder}", file1)
            and checkout(f"ls {result_folder}", test_folder)), "test2 FAIL"
    assert checkout(f"ls {result_folder}/test/", file2), "test2 FAIL"

"""2. Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
Доработать проект, добавив тест команды расчёта хеша (h).
Проверить, что хеш совпадает с рассчитанным командой crc32."""

import subprocess

from seminar2.test.checker import checkout

arc_folder = "/home/axidar/PycharmProjects/AutoQA/hw2/files/archives"
arc = "arc_hw2.7z"


def hash_get(folder: str, archive: str) -> str:
    sb = subprocess.run(f"cd {folder}; crc32 {archive}", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return sb.stdout[:-1].upper()


def test_hash_command():
    """Тестирование команды расчёта хэша"""
    assert checkout(f"cd {arc_folder}; 7z h {arc}", hash_get(arc_folder, arc)), "test1 FAIL"

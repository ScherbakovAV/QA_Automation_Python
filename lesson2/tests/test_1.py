import subprocess
import pytest


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


# ex3 через pytest
def test_step1():
    assert checkout("cd /home/axidar/tst; 7z a ../out/arx2",
                    "Everything is Ok"), "test1 FAIL"


# @pytest.mark.run_this
def test_step2():
    assert checkout("cd /home/axidar/out; 7z e arx2.7z -o/home/user/folder1 -y",
                    "Everything is Ok"), "test2 FAIL"


def test_step3():
    assert checkout("cd /home/axidar/out; 7z t arx2.7z",
                    "Everything is Ok"), "test3 FAIL"


"""Запуск с терминала:
python3 -m pytest -v test1.py
pytest -v test1.py / подробный вывод
pytest
pytest --collectonly / для подготовки к тестам
pytest -k test_step1 / для выполнения только выбранного теста
pytest -m run_this / для запуска нескольких тестов из разных модулей с использованием декоратора mark
pytest -x / для прерывания работы при выпадении ассерта
pytest --maxfail=2 -v / для продолжения проверок после определённого количества ошибок
pytest -s / для вывода всей информации (или --capture)
pytest --last-failed / запускает только тесты, упавшие при прошлом запуске
pytest -q / минимизирует вывод
pytest --showlocals / показывает локальные переменные
pytest --tb=no / вывод трассировки ошибок (no / line / short / long / native)
pytest --durations=1 / выводит самые медленные тесты"""

import yaml

from checkout import checkout_positive

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    """Создаём архив arx2 и проверяем его наличие в директории out"""
    res1 = checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(data["folder_out"]), "arx1.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    """Разархивируем архив arx2 в директорию folder1 и проверяем наличие там файлов test1, test2"""
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(data["folder_ext"]), item))
    assert all(res)


def test_step3():
    """Проверяем целостность архива arx2"""
    assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "Test1 Fail"


def test_step4():
    """Проверяем возможность обновления архива arx2"""
    assert checkout_positive("cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    """Проверяем удаление содержимого архива arx2"""
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
    assert all(res)


# def test_step6():


def test_step7():
    """Очищаем содержимое архива arx1"""
    assert checkout_positive("7z d {}/arx1.7z".format(data["folder_out"]), "Everything is Ok"), "Test1 Fail"


#  Проверить, тесты на каком наборе файлов пройдут быстрее: 5 по 2 Мб или 2 по 5 Мб.
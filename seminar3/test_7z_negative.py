import yaml

from checkout import checkout_negative

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_folders, make_files, make_bad_arx):
    """Разархивируем архив arx2 в директорию folder1 и проверяем наличие там файлов test1, test2"""
    assert checkout_negative("cd {}; 7z e badarx.7z -o{} -y".format(data["folder_out"], data["folder_ext"]), "ERROR"), "Test1 neg Fail"


def test_step2(clear_folders, make_folders, make_files, make_bad_arx):
    """Проверяем целостность архива arx2"""
    assert checkout_negative("cd {}; 7z t badarx.7z".format(data["folder_out"]), "ERROR"), "Test2 neg Fail"

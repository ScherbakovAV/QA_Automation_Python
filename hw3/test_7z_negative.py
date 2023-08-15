import yaml

from checkout import checkout_negative

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_folders, make_files, make_bad_arx):
    """Разархивируем архив в директорию и проверяем наличие там файлов"""
    assert checkout_negative(f'cd {data["folder_out"]}; 7z e badarx.{data["arc_type"]} -o{data["folder_ext"]} -y',
                             "ERROR"), 'Test 1 (neg) FAIL'


def test_step2(clear_folders, make_folders, make_files, make_bad_arx):
    """Проверяем целостность архива"""
    assert checkout_negative(f'cd {data["folder_out"]}; 7z t badarx.{data["arc_type"]}',
                             "ERROR"), 'Test 2 (neg) FAIL'


def test_step3(clear_folders, make_folders, make_files, make_bad_arx):
    """Создание архива с несуществующим расширением"""
    assert checkout_negative(f'cd {data["folder_in"]}; 7z a -t{data["bad_arc_type"]} '
                             f'{data["folder_out"]}/arx1.{data["bad_arc_type"]}',
                             "Unsupported archive type"), 'Test 3 (neg) FAIL'

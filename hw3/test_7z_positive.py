import yaml

from checkout import checkout_positive, getout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    """Создание архива и проверка его наличия в директории out"""
    res1 = checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                             f'{data["folder_out"]}/arx1.{data["arc_type"]}',"Everything is Ok")
    res2 = checkout_positive(f'ls {data["folder_out"]}', f'arx1.{data["arc_type"]}')
    assert res1 and res2, 'Test 1 FAIL'


def test_step2(clear_folders, make_files):
    """Разархивация архива в директорию и проверка наличия там файлов из архива"""
    res = []
    res.append(checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                                 f'{data["folder_out"]}/arx1.{data["arc_type"]}', 'Everything is Ok'))
    res.append(checkout_positive(f'cd {data["folder_out"]}; 7z e arx1.{data["arc_type"]} -o{data["folder_ext"]} -y',
                                 'Everything is Ok'))
    for item in make_files:
        res.append(checkout_positive(f'ls {data["folder_ext"]}', item))
    assert all(res), 'Test2 FAIL'


def test_step3():
    """Проверка целостности архива"""
    assert checkout_positive(f'cd {data["folder_in"]}; 7z t {data["folder_out"]}/arx1.{data["arc_type"]}',
                             'Everything is Ok'), 'Test 3 FAIL'


def test_step4():
    """Проверка возможности обновления архива"""
    assert checkout_positive(f'cd {data["folder_in"]}; 7z u {data["folder_out"]}/arx1.{data["arc_type"]}',
                             'Everything is Ok'), 'Test 4 FAIL'


def test_step5(clear_folders, make_files):
    """Проверка удаления содержимого архива arx2"""
    res = []
    res.append(
        checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                          f'{data["folder_out"]}/arx1.{data["arc_type"]}', "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive(f'cd {data["folder_out"]}; 7z l arx1.{data["arc_type"]}', item))
    assert all(res), 'Test 5 FAIL'


def test_step6(clear_folders, make_files, make_subfolder):
    """Проверка разархивирования файлов с сохранением структуры директорий (x)
        и команды вывода списка файлов (l) в архиве"""
    checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                      f'{data["folder_out"]}/arx1.{data["arc_type"]}', "")
    res = []
    res.append(checkout_positive(f'cd {data["folder_out"]}; 7z x arx1.{data["arc_type"]} -o{data["folder_ext"]} -y',
                                 "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive(f'cd {data["folder_out"]}; 7z l arx1.{data["arc_type"]}', item))
        res.append(checkout_positive(f'ls {data["folder_ext"]}', item))
    res.append(checkout_positive(f'ls {data["folder_ext"]}', make_subfolder[0]))
    res.append(checkout_positive(f'cd {data["folder_ext"]}/{make_subfolder[0]}; ls', make_subfolder[1]))
    print(res)
    assert all(res), 'test 6 FAIL'


def test_step7():
    """Очистка содержимое архива arx1"""
    assert checkout_positive(f'7z d {data["folder_out"]}/arx1.{data["arc_type"]}',
                             'Everything is Ok'), 'Test 7 FAIL'


def test_step8(make_folders, clear_folders, make_files):
    """Тестирование команды расчёта хэша"""
    checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                      f'{data["folder_out"]}/arx1.{data["arc_type"]}', "")
    assert checkout_positive(f'cd {data["folder_out"]}; 7z h arx1.{data["arc_type"]}',
                             getout(data["folder_in"], 'arx1.{data["arc_type"]}')), 'test 8 FAIL'

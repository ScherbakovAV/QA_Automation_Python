import inspect
import random
import string
import pytest
import yaml
from datetime import datetime

from checkout import checkout_positive

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout_positive(f'mkdir {data["folder_in"]} {data["folder_out"]} '
                             f'{data["folder_ext"]} {data["folder_badarx"]}', "")


@pytest.fixture()
def clear_folders():
    return checkout_positive(f'rm -rf {data["folder_in"]}/* {data["folder_out"]}/* '
                             f'{data["folder_ext"]}/* {data["folder_badarx"]}/*', "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count_file"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(f'cd {data["folder_in"]}; dd if=/dev/urandom of={filename} '
                             f'bs={data["size_file"]} count=1 iflag=fullblock', ''):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive(f'cd {data["folder_in"]}; mkdir {subfoldername}', ''):
        return None, None
    if not checkout_positive(f'cd {data["folder_in"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} '
                             f'bs=1M count=1 iflag=fullblock', ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx():
    """Написать фикстуру, создающую перед шагом теста битый архив
    и удаляющую его после завершения шага теста."""
    checkout_positive(f'cd {data["folder_in"]}; 7z a -t{data["arc_type"]} '
                      f'{data["folder_badarx"]}/badarx.{data["arc_type"]}', "")
    checkout_positive(f'truncate -s 1 {data["folder_badarx"]}/badarx.{data["arc_type"]}', "")
    yield
    checkout_positive(f'rm -f {data["folder_badarx"]}/badarx.{data["arc_type"]}', "")


@pytest.fixture(autouse=True)
def write_stat():
    if not checkout_positive(f'ls', 'stat.txt'):
        checkout_positive(f'echo > stat.txt; ls', 'stat.txt')
    time_now = datetime.now().strftime("%d %B %Y - %H:%M:%S.%f")

    with (open('config.yaml') as f_conf,
          open('/proc/loadavg') as f_proc):
        info = yaml.safe_load(f_conf)
        proc_load = f_proc.read()

    files_count = info['count_file']
    file_size = info['size_file']

    with open('stat.txt', 'a', encoding='utf-8') as f_stat:
        f_stat.write(f'Stat at {time_now}: {files_count=}, {file_size=}, {proc_load=}\n')

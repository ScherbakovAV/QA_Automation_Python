import random
import string
import pytest
import yaml
from datetime import datetime

from sshcheckers import ssh_checkout, ssh_getout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return ssh_checkout(data["host"], data["user"], "123",
                        "mkdir {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                   data["folder_badarx"]), "")


@pytest.fixture()
def clear_folders():
    return ssh_checkout(data["host"], data["user"], "123",
                        "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                            data["folder_badarx"]), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count_file"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout(data["host"], data["user"], "123",
                        "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"],
                                                                                               filename,
                                                                                               data["size_file"]),
                        ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not ssh_checkout(data["host"], data["user"], "123", "cd {}; mkdir {}".format(data["folder_in"], subfoldername),
                        ""):
        return None, None
    if not ssh_checkout(data["host"], data["user"], "123",
                        "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
                                                                                                  subfoldername,
                                                                                                  testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx():
    """Написать фикстуру, создающую перед шагом теста битый архив
    и удаляющую его после завершения шага теста."""
    ssh_checkout(data["host"], data["user"], "123",
                 "cd {}; 7z a {}/badarx.7z".format(data["folder_in"], data["folder_badarx"]), "Everything is Ok")
    ssh_checkout(data["host"], data["user"], "123", "truncate -s 1 {}/badarx.7z".format(data["folder_badarx"]),
                 "Everything is Ok")
    yield
    ssh_checkout(data["host"], data["user"], "123", "rm -f {}/badarx.7z".format(data["folder_badarx"]), "")


@pytest.fixture()
def start_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def save_log(starttime, name):
    # print(ssh_getout(data["host"], data["user"], "123",
    #            f'journalctl --since {starttime}'))
    with open(name, 'w') as file:
        file.write(ssh_getout(data["host"], data["user"], "123", f'journalctl --since {starttime}'))
    return True

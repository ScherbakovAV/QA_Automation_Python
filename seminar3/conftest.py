import random
import string
import pytest
import yaml

from checkout import checkout_positive

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout_positive("mkdir {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"], data["folder_badarx"]), "")


@pytest.fixture()
def clear_folders():
    return checkout_positive("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"], data["folder_badarx"]), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count_file"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"], filename, data["size_file"]),
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx():
    """Написать фикстуру, создающую перед шагом теста битый архив
    и удаляющую его после завершения шага теста."""
    checkout_positive("cd {}; 7z a {}/badarx.7z".format(data["folder_in"], data["folder_badarx"]), "Everything is Ok")
    checkout_positive("truncate -s 1 {}/badarx.7z".format(data["folder_badarx"]), "Everything is Ok")
    yield
    checkout_positive("rm -f {}/badarx.7z".format(data["folder_badarx"]), "")

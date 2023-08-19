import yaml

from conftest import save_log
from sshcheckers import upload_files, ssh_checkout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step0():
    """Деплой"""
    res = []
    upload_files(data["host"], data["user"], "123",
                 f"{data['local_path']}/p7zip-full.deb", f"{data['remote_path']}p7zip-full.deb")
    res.append(ssh_checkout(data["host"], data["user"], "123",
                            f"echo '123' | sudo -S dpkg -i {data['remote_path']}p7zip-full.deb", "Настраивается пакет"))
    res.append(ssh_checkout(data["host"], data["user"], "123", "echo '123' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res), "Test0 Fail"


def test_step1(make_folders, clear_folders, make_files, start_time):
    """Создаём архив и проверяем его наличие в директории out"""
    res1 = ssh_checkout(data["host"], data["user"], "123",
                        "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"
    res2 = ssh_checkout(data["host"], data["user"], "123", "ls {}".format(data["folder_out"]), "arx1.7z"), "Test1 Fail"
    save_log(start_time, data["stat_file"])
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, start_time):
    """Разархивируем архив arx2 в директорию folder1 и проверяем наличие там файлов test1, test2"""
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "123",
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], "123",
                            "cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                            "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "123", "ls {}".format(data["folder_ext"]), item))
    save_log(start_time, data["stat_file"])
    assert all(res)


def test_step3():
    """Проверяем целостность архива arx2"""
    assert ssh_checkout(data["host"], data["user"], "123",
                        "cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step4():
    """Проверяем возможность обновления архива arx2"""
    assert ssh_checkout(data["host"], data["user"], "123",
                        "cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files, start_time):
    """Проверяем удаление содержимого архива arx2"""
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "123",
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(
            ssh_checkout(data["host"], data["user"], "123", "cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
    save_log(start_time, data["stat_file"])
    assert all(res)


# def test_step6():


def test_step7():
    """Очищаем содержимое архива arx1"""
    assert ssh_checkout(data["host"], data["user"], "123", "7z d {}/arx1.7z".format(data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"

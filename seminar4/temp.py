import subprocess

import yaml
from datetime import datetime
from seminar4.sshcheckers import ssh_getout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def save_log(starttime, name):
    out = ssh_getout(data["host"], data["user"], "123",
               f'echo "123" | sudo -S journalctl --since "{starttime}"')
    print(out)
    return subprocess.run(f'echo "123" | sudo -S echo "{out}" > {name}', shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    # with open(name, 'w') as file:
    #     file.write(ssh_getout(data["host"], data["user"], "123",
    #                f'echo "123" | sudo -S journalctl --since "{starttime}"'))


print(save_log(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data["stat_file"]))

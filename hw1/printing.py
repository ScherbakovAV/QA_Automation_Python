from scripts.ex2 import test_command


def print_command_test(cmd: str, text: str, del_punc: bool = False) -> None:
    work_mode = 1 if del_punc else 0
    result = test_command(cmd, text, mode=work_mode)
    print(f'{result} in mode {work_mode} | {text=} | {cmd=}')

from printing import print_command_test


if __name__ == '__main__':
    command1, res1 = 'ls /etc', 'sudoers'
    command2, res2 = 'cat /home/axidar/PycharmProjects/AutoQA/hw1/scripts/ex1.py', 'cmd: str, text: str'
    res3 = 'resultreturncode'
    print_command_test(command1, res1)
    print_command_test(command2, res2)
    print_command_test(command2, res1)
    print_command_test(command2, res2, True)
    print_command_test(command2, res3, True)

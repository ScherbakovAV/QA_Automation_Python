import time


def retry(func):
    def wrapper():
        try:
            func()
        except:
            print('retrying...')
            time.sleep(1)
            func()
    return wrapper()


@retry
def might_fail():
    print('might fail')
    raise Exception


might_fail()

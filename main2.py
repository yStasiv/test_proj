"""Test"""


def calc(string: str) -> int:
    return len(string.split(' '))


if __name__ == '__main__':
    print(calc('abc Gdd hfd Hfcv'))

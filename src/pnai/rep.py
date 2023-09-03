def read_(arg: str) -> str:
    return arg


def eval_(arg: str) -> str:
    return arg


def print_(arg: str) -> str:
    return arg


def rep(arg: str) -> str:
    return print_(eval_(read_(arg)))

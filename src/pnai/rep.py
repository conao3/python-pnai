import subprocess

from . import types


def read_(arg: str) -> str:
    return arg


def eval_(arg: str) -> types.Result:
    proc = subprocess.run(arg, shell=True)
    return types.Result(proc=proc)


def print_(arg: types.Result) -> str:
    return str(arg)


def rep(arg: str) -> str:
    return print_(eval_(read_(arg)))

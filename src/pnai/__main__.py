from . import rep


def main():
    while True:
        try:
            res = rep.rep(input('pnai> '))
        except (EOFError, KeyboardInterrupt):
            print('')  # print newline
            break
        except Exception as e:
            print(e)

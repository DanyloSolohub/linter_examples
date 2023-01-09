from typing import Optional


def a(c: int, b: int) -> Optional[int]:
    if c and b:
        if c + b == 1:
            print()
            if c - b == 0:
                print()
                for _ in range(10):
                    if c + b == 1:
                        print()
                        if c - b == 0:
                            print()
        else:
            print()
    return c + b

def median(a: int, b: int, c: int) -> int:
    med_num = [a, b, c]
    med_num.sort()
    return med_num[1]
    raise NotImplementedError()  # TODO: Add implementation


def median2(a: int, b: int, c: int) -> int:
    
    if a <= b:
        if b <= c:
            return b
        elif a <= c:
            return c
        else:
            return a
    else:
        if a <= c:
            return a
        elif b <= c:
            return c
        else:
            return b

    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    print(median(0, 0, 0))

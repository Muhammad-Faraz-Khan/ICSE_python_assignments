def transform_to_dual(dec: int) -> str:
    """Transforms a given decimal number to it's dual representation."""
    
    if dec == 0:
        return "0"

    binary = ""

    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec = dec // 2

    return binary

    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    pass

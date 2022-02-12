def int2bin(intN, n):
    """
    Returns a length n boolean list representation of intN appropriately truncated or padded
    """
    pattern = '{:0' + str(n) + 'b}'
    binStrN = pattern.format(intN)[-n:]
    return [int(i) for i in binStrN]


def bin2int(binList):
    """
    Returns an integer representation of binList
    """
    intN = 0
    for b in binList:
        intN = (intN * 2) + b
    return intN

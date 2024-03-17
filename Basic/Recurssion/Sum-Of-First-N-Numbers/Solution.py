def sumFirstN(n: int) -> int:

    # Write your code here.

    if n == 0:

        return 0

    else:

        return n + sumFirstN(n-1)
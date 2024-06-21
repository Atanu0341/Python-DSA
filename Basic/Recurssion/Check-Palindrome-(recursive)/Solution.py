def func(i, n, string):
    if i >= n / 2:
        return True

    if string[i] != string[n - i - 1]:
        return False

    return func(i + 1, n, string)

def isPalindrome(string: str) -> bool:
    return func(0, len(string), string)
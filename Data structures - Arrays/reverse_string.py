"""
Create a function that reverses a string
"""

def reverse_string(str_rev):
    """
    Reverses a string
    """
    new_str = []
    if isinstance(str_rev, str):
        if len(str_rev) > 1:
            for i in range(len(str_rev) - 1, -1, -1):
                new_str.append(str_rev[i])
            return "".join(new_str)
        else:
            return str_rev
    else:
        return None


def reverse_string_easy(str_rev):
    """Reverses a string"""
    if isinstance(str_rev, str):
        if len(str_rev) > 1:
            return str_rev[::-1]
        else:
            return str_rev
    else:
        return None

TEST_STR = "Hi, my name is XXXX"
print(reverse_string(TEST_STR))
print(reverse_string_easy(TEST_STR))


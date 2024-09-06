def min_string(a, b):
    if len(a) > len(b):
        return f"{b}{a}{b}"
    else:
        return f"{a}{b}{a}"


a = "U"
b = "False"

print(min_string(a, b))

def check_integers(name="NoName", *args):
    print(name)
    for item in args:
        if type(item) != int:
            return False
    return True

lists1 = [1, 2, 3]
list2 = ["a", "b", 1, 5, "c"]

print(check_integers("Petras", 1, 2, 3))
print(check_integers("p", "o", "i", 1, 2, 9))
print(check_integers("Johans", "1", "2"))
print(check_integers(5))

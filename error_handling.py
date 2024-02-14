list1 = [12, 5, 3, 4, 56, 12]
list2 = [0, 2, 3, 0, "12", 78, 12]

for index, item in enumerate(list1):
    try:
        result = item / list2[index]
        print(result)
    except (ZeroDivisionError, TypeError, IndexError):
        print("Infifnity")
    except TypeError:
        print("can't divide int by string")
    except IndexError:
        print("Too many items")




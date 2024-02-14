list_1 = ["a", "b", "c", "d"]

def str_added (input_list, ending="String"):
    list2 = []
    for item in input_list:
        list2.append(str(item) + ending)
    return list2

print(str_added(list_1,  "String"))
print(str_added([1, 2, 3, 4, 5],  "Anything"))
print(str_added(["john", "megan", "paul", "hoko"]))


evens = []
for i in range(11):
    if i % 2 == 0:
        evens.append(i)

print(evens)

evens2 = [i for i in range(11) if i % 2 == 0]
print(evens2)

asd = [for k in range(10)]

times_three = []
for i in range(11):
    times_three.append(i*3)

tuple(123)
print(times_three)
times_three2 = tuple([i * 3 for i in range(10)])
print(times_three2)

print(evens2)

chars = ["a", "b", "c", "d", "e", "f", "g", "k"]

dict_compr = {c: i for c, g for k zip in range(11)}

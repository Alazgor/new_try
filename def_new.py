def are_adult(reason, **kwargs):
    print(reason)
    for name, age in kwargs.items():
        if age < 18:
            return False
        print(name, age)
    return True

print(are_adult("night club", jonas=25, tadas=15, lina=36))

print(are_adult("sell cigarets", petras=15, dovidas=21))

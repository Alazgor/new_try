import random

pin_code = random.randint(1000, 9999)
for item in range (1000, 10000):
    if item == pin_code:
        print(f"It's correct combination {item}")


import random
min = int(input("input MIN: "))
max = int(input("Input MAX: "))
quantity = int(input("Input quantity: "))

def get_numbers_ticket(min, max, quantity):
    if min < max and quantity >=1:
        spam = list(range(min, max+1))
        result = random.sample(spam, quantity)
        return sorted(result)
    else:
        spam = []
        print("Incorrect input ")
        return spam

print(get_numbers_ticket(min,max,quantity))

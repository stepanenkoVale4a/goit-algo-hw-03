import random
min = int(input("input MIN: ")) #Вводимо мінімальну границю
max = int(input("Input MAX: ")) #Max
quantity = int(input("Input quantity: "))

def get_numbers_ticket(min, max, quantity):
    if min < max and min < quantity < max:
        spam = list(range(min, max+1))
        result = random.sample(spam, quantity)
        return sorted(result)
    else:
        spam = []
        print("Incorrect input ")
        return spam

print(get_numbers_ticket(min,max,quantity))

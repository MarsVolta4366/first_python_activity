def hello():
    print("Good day!")

hello()

def pack(item1, item2, item3):
    return [item1, item2, item3]

print(pack("A thing", "Another thing", "A final thing"))

def eat_lunch(food_items):
    if len(food_items) == 0:
        print("My lunchbox is empty!") 
    else:
        for i in range(len(food_items)):
            if i == 0:
                print(f"First I eat {food_items[i]}")
            else:
                print(f"Next I eat {food_items[i]}")

eat_lunch(["Apple", "Orange", "Sandwich", "Oreos"])
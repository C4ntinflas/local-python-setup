def hello():
    print("Hello! Welcome to the functions practice.")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        for i, food in enumerate(food_list):
            if i == 0:
                print(f"First I eat {food}.")
            else:
                print(f"Next I eat {food}.")

if __name__ == "__main__":
    hello()  # Call the hello function

    packed_list = pack("apple", "sandwich", "cookie")  
    print(packed_list)  

    eat_lunch(packed_list)  

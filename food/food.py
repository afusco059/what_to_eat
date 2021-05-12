import random

chinese_food = ["House of China", "Imperial Garden", "Golden Hunan", "Main Moon", "Chinatown Inn",]
Buffet_food = ["Royale Grill", "Golden Corral", "Ponderosa"]
japanese_food = ["Izumi", "Mizu", "Tokyo House", "Sakura", "Asuka"]
mexican_food = ["Plaza Mexico", "Los Gallos", "Jalisco's"]
pizza_food =["Belleria", "Rise Pies", "Brick oven"]
fast_food = ["Chic Fil A", "Sonic", "Hardy's"]
italian_food = ["Salvatores", "Scarsellas", "Nicolinni's"]

cuisine_choice_responses = ["Oh Snap great idea. ", "Oh yeah sure that sounds great. ", "Oh yeah all them carbs are mine today ", "One of my favs. ", "Looks like I'm going to struggle with all this food. "]

random_response = random.choice(cuisine_choice_responses)

def Hola():
    print("Hello there, having trouble deciding what your in the mood for, I got you")
    cuisine_choice = input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Japanese\n3 = Mexican\n4 = Pizza \n5 = Fast Food\n6 = Italian\n7 = Buffet \n8 = I Don't Know!\nPlease enter a number: ")
    if cuisine_choice == "1":
        print(random_response+"You should eat at: "+random.choice(chinese_food))
    elif cuisine_choice == "2":
        print(random_response+"You should eat at: "+random.choice(japanese_food))
    elif cuisine_choice == "3":
        print(random_response+"You should eat at: "+random.choice(mexican_food))
    elif cuisine_choice == "4":
        print(random_response+"You should eat at: "+random.choice(pizza_food))
    elif cuisine_choice == "5":
        print(random_response+"You should eat at: "+random.choice(fast_food))
    elif cuisine_choice == "6":
        print(random_response+" You should eat at: "+random.choice(italian_food))
    elif cuisine_choice == "7":
        print(random_response+" You should eat at: "+random.choice(Buffet_food))
    elif cuisine_choice == "8":
        my_random_choice = random.randint(1,8)
        if my_random_choice == 1:
            print(random_response+"You should eat at: "+random.choice(chinese_food))
        elif my_random_choice == 2:
            print(random_response+"You should eat at: "+random.choice(japanese_food))
        elif my_random_choice == 3:
            print(random_response+"You should eat at: "+random.choice(mexican_food))
        elif my_random_choice == 5:
            print(random_response+"You should eat at: "+random.choice(pizza_food))
        elif my_random_choice == 6:
            print(random_response+"You should eat at: "+random.choice(fast_food))
        elif cuisine_choice == 7:
             print(random_response+" You should eat at: "+random.choice(Buffet_food))
        else:
            print(random_response+" You should eat at: "+random.choice(italian_food))
    else:
        print("\033[1;32;47m You did not select a number. Please try again. ")
        
        Hola()

Hola() 
money = 550
water = 400
milk = 540
beans = 120
cups = 9

def buy_coffee():
    global money, water, milk, beans, cups
    user_coffee_type = input("What kind of coffee do you want to order: 1 - espresso ($4), 2 - latte ($7), or 3 - cappuccino ($6)?\n")
    # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
    if user_coffee_type == "1":
        if water >= 250:
            if beans >= 16:
                if cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    money += 4
                    water -= 250
                    beans -= 16
                    cups -= 1
                else:
                    print("Sorry, not enough cups!")
            else:
                print("Sorry, not enough beans!")
        else:
            print("Sorry, not enough water!")
            
    # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
    if user_coffee_type == "2":
        if water >= 350:
            if milk >= 75:   
                if beans >= 20:
                    if cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        money += 7
                        water -= 350
                        milk -= 75
                        beans -= 20
                        cups -= 1
                    else:
                        print("Sorry, not enough cups!")
                else:
                    print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough milk!")
        else:
            print("Sorry, not enough water!")
    # And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
    if user_coffee_type == "3":
        if water >= 200:
            if milk >= 100:
                if beans >= 12:
                    if cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        money += 6
                        water -= 200
                        milk -= 100
                        beans -= 12
                        cups -= 1
                    else:
                        print("Sorry, not enough cups!")
                else:
                    print("Sorry, not enough beans!")
            else:
                print("Sorry, not enough milk!")
        else:
            print("Sorry, not enough water!")

def fill_coffee():
    global money, water, milk, beans, cups
    # print("The coffee machine has:\n", str(water), "ml of water\n", str(milk), "ml of milk\n", str(beans), "g of coffee beans and\n", str(cups), "pcs of disposable cups\n", str(money), "of money.")
    # print("This program adds water, milk, coffee and disposable cups dinto the coffee machine.")
    fill_water = int(input("How much WATER do you want to add into the coffee machine?\n"))
    fill_milk = int(input("How much MILK do you want to add into the coffee machine?\n"))
    fill_coffee = int(input("How much COFFEE BEANS do you want to add into the coffee machine?\n"))
    fill_cups = int(input("How many DISPOSABLE CUPS do you want to add into the coffee machine?\n"))
    water += fill_water
    milk += fill_milk
    beans += fill_coffee
    cups += fill_cups
    # print("The coffee machine has:\n", str(water), "ml of water\n", str(milk), "ml of milk\n", str(beans), "g of coffee beans and\n", str(cups), "pcs of disposable cups\n", str(money), "of money.")

def take():
    global money, water, milk, beans, cups
    # print("The coffee machine has:\n", str(water), "ml of water\n", str(milk), "ml of milk\n", str(beans), "g of coffee beans and\n", str(cups), "pcs of disposable cups\n", str(money), "of money.\n")
    print("I gave you $" + str(money) + "\n")
    money -= money
    # print("The coffee machine has:\n", str(water), "ml of water\n", str(milk), "ml of milk\n", str(beans), "g of coffee beans and\n", str(cups), "pcs of disposable cups\n", str(money), "of money.")

def remaining():
    global money, water, milk, beans, cups
    print("The coffee machine has:\n", str(water), "ml of water\n", str(milk), "ml of milk\n", str(beans), "g of coffee beans\n", str(cups), "pcs of disposable cups\n",
    str(money), "of money")

def main():
    while True:
        user_input = input("Write action (buy, fill, take, remaining, exit):\n")
        if user_input == "buy":
            buy_coffee()
        if user_input == "fill":
            fill_coffee()
        if user_input == "take":
            take()
        if user_input == "remaining":
            remaining()
        if user_input == 'exit':
            break

main()
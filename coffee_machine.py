water = 400
milk = 540
beans = 120
cups = 9
money = 550


def remaining():
    global water, milk, beans, cups, money
    print()
    print('The coffee machine has:')
    print(water, 'ml of water')
    print(milk, 'ml of milk')
    print(beans, 'g of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')
    print()


def buy():
    global water, milk, beans, cups, money, action
    coffee_type = input('What do you want to buy? 1- espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

    if coffee_type == '1':
        if water >= 250 and beans >= 16 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
        elif water < 250:
            print('Sorry, not enough water!')
        elif beans < 16:
            print('Sorry, not enough coffee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')

    elif coffee_type == '2':
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
        elif water < 350:
            print('Sorry, not enough water!')
        elif milk < 75:
            print('Sorry, not enough milk!')
        elif beans < 20:
            print('Sorry, not enough coffee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')

    elif coffee_type == '3':
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
        elif water < 200:
            print('Sorry, not enough water!')
        elif milk < 100:
            print('Sorry, not enough milk!')
        elif beans < 12:
            print('Sorry, not enough coffee beans!')
        elif cups < 1:
            print('Sorry, not enough cups!')

    elif coffee_type == 'back':
        pass


def fill():
    global water, milk, beans, cups, money
    water_add = int(input('Write how many ml of water do you want to add:?'))
    water += water_add

    milk_add = int(input('Write how many ml of milk do you want to add:?'))
    milk += milk_add

    beans_add = int(input('Write how many grans of coffee beans do you want to add:?'))
    beans += beans_add

    cups_add = int(input('Write how many disposable cups of coffee do you want to add:?'))
    cups += cups_add


def take():
    global money
    print('I gave you $%d', money)
    money -= money


def end():
    exit()


while True:
    action = input('Write action (buy, fill, take, remaining, exit):')

    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        end()

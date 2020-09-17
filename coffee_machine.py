class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def user_interaction(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')

            if action == 'buy':
                coffee.buy()
            elif action == 'fill':
                coffee.fill()
            elif action == 'take':
                coffee.take()
            elif action == 'remaining':
                coffee.remaining()
            elif action == 'exit':
                coffee.end()

    def remaining(self):
        print()
        print('The coffee machine has:')
        print(self.water, 'ml of water')
        print(self.milk, 'ml of milk')
        print(self.beans, 'g of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')
        print()

    def buy(self):
        coffee_type = input('What do you want to buy? 1- espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

        if coffee_type == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            elif self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')

        elif coffee_type == '2':
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            elif self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')

        elif coffee_type == '3':
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            elif self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')

        elif coffee_type == 'back':
            pass

    def fill(self):
        water_add = int(input('Write how many ml of water do you want to add:?'))
        self.water += water_add

        milk_add = int(input('Write how many ml of milk do you want to add:?'))
        self.milk += milk_add

        beans_add = int(input('Write how many grans of coffee beans do you want to add:?'))
        self.beans += beans_add

        cups_add = int(input('Write how many disposable cups of coffee do you want to add:?'))
        self.cups += cups_add

    def take(self):
        print('I gave you $%d', self.money)
        self.money -= self.money

    def end(self):
        exit()


coffee = CoffeeMachine(400, 540, 120, 9, 550)
coffee.user_interaction()
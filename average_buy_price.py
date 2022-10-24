purchases = []
counter = 0

def main():
    isRunning = True
    while isRunning == True:
        init_purchase()
        choice = input('Do you want to add another purchase? (Y/N): ').lower()
        while (choice == '') or (choice[0] != 'y') and (choice[0] != 'n'):
            choice = input('Do you want to add another purchase? (Y/N): ').lower()
        if choice[0] == 'y':
                isRunning = True
        if choice[0] == 'n':
                isRunning = False
                avg_calc()

def init_purchase():
    global counter
    while True:
        try:
            buy_price = int(input(f'Please enter the buy price for purchase number {counter + 1}: '))
            break
        except ValueError:
            print('Please enter a number value for your buy price!')
    purchases.append(buy_price)
    counter += 1
    print(*purchases, sep='\n')
    print(f'Number of purchases: {counter}')
    
def avg_calc():
    result = int(sum(purchases) / counter)
    print(f'Your average buy price is: {result}€')
    print(f'Number of purchases: {counter}')

if __name__ == '__main__':
    main()


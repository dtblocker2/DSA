class VendingMachine:
    def __init__(self, numItems, itemPrice):
        self.numItems = numItems
        self.itemPrice = itemPrice

    def buy(self, itemRequested, coinsGiven):
        if (itemRequested > self.numItems):
            raise ValueError('Not enough items in the machine')

        if (itemRequested*self.itemPrice > coinsGiven):
            raise ValueError('Not enough coins')
        
        self.numItems -= itemRequested
        return (coinsGiven-self.itemPrice*itemRequested)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)
    output = []

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            # fptr.write(str(change) + "\n")
            output.append(str(change))
        except ValueError as e:
            # fptr.write(str(e) + "\n")
            output.append(str(e))


    # fptr.close()
    print(output)
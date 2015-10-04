def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print "Sorry we don't have %s" % (fruit)
    else:
        cost = fruitPrices[fruit] * numPounds
        print "That'll be %f please" % (cost)

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}        
buyFruit('apples',2.4)
buyFruit('coconuts',2)
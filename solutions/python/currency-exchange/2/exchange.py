def exchange_money(budget, exchange_rate):
    '''budget: the amount of money you want to exchange; exchange_rate:the currency to echange the value'''
    result = budget/exchange_rate
    return result
sino = exchange_money(127.5, 1.2)
print(sino)
    

def get_change(budget, exchanging_value):
    change = budget - exchanging_value
    return change
print(get_change(127.5, 120))


def get_value_of_bills(denomination, number_of_bill):
    total = denomination * number_of_bill
    return total
print(get_value_of_bills(5, 128))
    
    
def get_number_of_bills(amount, denomination):
    number = amount // denomination
    return number
print(get_number_of_bills(127.5, 5))
    

def get_leftover_of_bills(amount, denomination):
    resultado = amount % denomination
    return resultado
print(get_leftover_of_bills(127.5, 20))
    

def exchangeable_value(budget, exchange_rate, spread, denomination):
    #calcular cuanto es al cambio
    percentage = spread/100
    maximum_value = (exchange_rate*percentage) + exchange_rate
    amount = budget/maximum_value
    resto = amount%denomination
    return amount-resto
print(exchangeable_value(127.25, 1.20, 10, 5))
    
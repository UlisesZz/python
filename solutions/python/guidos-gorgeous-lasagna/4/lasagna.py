EXPECTED_BAKE_TIME = 40
'''The time the lasagna should be in oven'''

def bake_time_remaining(minutesInOven):
    '''Calculate the remaining timeof the lasagna'''
    return EXPECTED_BAKE_TIME - minutesInOven

#print(bake_time_remaining(25))


def preparation_time_in_minutes(number_of_layers):
    '''Calculate the time that the number of layer affect the time in oven'''
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Calculate de time elapsed time'''
    minutesThisLasagnaShoulBeInOven = preparation_time_in_minutes(number_of_layers)
    elapsedTime = minutesThisLasagnaShoulBeInOven + elapsed_bake_time
    return elapsedTime 

print(elapsed_time_in_minutes(8, 20))
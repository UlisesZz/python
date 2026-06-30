"""Functions used in preparing Guido's gorgeous lasagna."""
EXPECTED_BAKE_TIME = 40
'''The time the lasagna should be in oven'''

def bake_time_remaining(minutes_in_oven):
    '''Calculate the remaining timeof the lasagna'''
    return EXPECTED_BAKE_TIME - minutes_in_oven

#print(bake_time_remaining(25))


def preparation_time_in_minutes(number_of_layers):
    '''Calculate the time that the number of layer affect the time in oven'''
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Calculate de time elapsed time'''
    minutes_lasagna_shoul_in_oven = preparation_time_in_minutes(number_of_layers)
    elapsed_time = minutes_lasagna_shoul_in_oven + elapsed_bake_time
    return elapsed_time 

print(elapsed_time_in_minutes(8, 20))
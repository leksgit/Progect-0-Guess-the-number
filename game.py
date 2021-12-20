""" "Guess the number" game"""
import numpy as np
import time
from numpy.lib.function_base import average


def game_core(number: int = 1) -> int:
    """ Found random number in diapason
    Args:
        number (int, optional): The random number to be found. Defaults to 1.

    Returns:
        int: number of attempts
    """

    attempts = 0   # number of attempts
    prdict_min = 1  # minimal random number
    prdict_max = 101  # maximum random number
    
    if number < prdict_min or number > prdict_max:
        raise ValueError(f'Out of range! Min: {prdict_min} Max: {prdict_max}')
    
    while True:
        attempts+=1
        
        predict_number = (prdict_max + prdict_min) // 2
        predict_average_number = predict_number // 2
        if number > predict_number:
            prdict_min = predict_number
            if number > (predict_number + predict_average_number):
                prdict_min = predict_number + predict_average_number
        elif number < predict_number:
            prdict_max = predict_number
            if number < (predict_number - predict_average_number):
                prdict_max = predict_number - predict_average_number
        else:
            break
        
        

    # Count attempts before success found

    return attempts

def score_game(game_core) -> int:
    """For how many attempts, on average, per 1000 approaches, our algorithm guesses
    Args:
        random_predict ([type]): function for Guess the number
    Returns:
        int: average number of attempts
    """

    count_ls = []  # list attumps
    np.random.seed(1)  # fix seed for repeatable
    random_array = np.random.randint(1, 101, size=(1000))  # generate random number for guesses
    
    start_time = time.time()

    for number in random_array:
        count_ls.append(game_core(number))

    score = round(float(np.mean(count_ls)),2)  # average number of attempts

    execution_time = round((time.time() - start_time),4)
    print(f'Your algorithm guesses the number on average in: {score} tries, time {execution_time} seconds')
    return(score)

score_game(game_core)
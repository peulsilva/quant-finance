import numpy as np
from src.egg import Egg

def eggs_experiment(
    num_eggs : int,
    building_size : int,
    step : int
):
    highest_floor = np.random.randint(1, building_size + 1)
    eggs = [Egg(highest_floor) for i in range(num_eggs)]

    floor = int(building_size/step)
    tried_floors = []

    min, max = 0, building_size
    # O(log_{step} N)
    while len(eggs)>1 and max>min:
        tried_floors.append(floor)
        eggs[0].throw(floor)

        if eggs[0].is_broken():
            max = floor
        else:
            min = floor
        
        delta = int((max-min)/step)
        if delta == 0:
            eggs=[Egg(highest_floor)]
            break

        if eggs[0].is_broken():
            eggs.pop(0)
            floor -= delta
        else:
            floor += delta

    if max <= min:
        broken_floor = max

    else:
        # O(N)
        if len(tried_floors) < 2:
            floor = 0
        else:
            floor = tried_floors[-2]
        while len(eggs) > 0 :
            tried_floors.append(floor)
            eggs[0].throw(floor)

            if eggs[0].is_broken():
                eggs.pop(0)
            else:
                floor += 1
        broken_floor = tried_floors[-2]

        
    num_tries = len(tried_floors)
    

    if broken_floor != highest_floor:
        import pdb
        pdb.set_trace()

    return num_tries, broken_floor, highest_floor
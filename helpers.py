from random import randint

global current_wait_time

def pick_random_time(wait_times):
    random_time = randint(0, len(wait_times) -1)
    wait_times[random_time]['in_use'] = True

def reset_wait_time(currently_used_wait_time):
    print(currently_used_wait_time)
    currently_used_wait_time[0]['in_use'] = False

def set_wait_time(wait_times):
    for index in range(len(wait_times)):
        for key in wait_times[index]:
            if wait_times[index][key] == True:
                current_wait_time = wait_times[index]['time']
                reset_wait_time(wait_times)
    pick_random_time(wait_times)
    return current_wait_time

    
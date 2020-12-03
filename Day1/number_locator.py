from random import shuffle
import numpy
import time


def is_sorted(data):
    '''Check if neatly aligned and in order - Keep it clean!'''
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bogosort(data) -> list:
    '''Just fuck the code up'''
    while not is_sorted(data):
        shuffle(data)
    return data


nums_list = open(r'input.txt', "r")
nums_list_entries = nums_list.read().splitlines()
nums_list.close()

start_time = time.time()


least_optimised_data = bogosort(nums_list_entries)
print('wow cant believe this is done')
print("--- %s This took a whopping seconds ---" % (time.time() - start_time))
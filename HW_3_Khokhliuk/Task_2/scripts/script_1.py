import pickle
import numpy


def get_num_list(file_name):
    file = open(file_name, 'rb')
    num_list = pickle.load(file)
    file.close()
    print(num_list)
    return num_list



def count_average(num):

    return numpy.mean(num)


print(count_average(get_num_list("task2")))

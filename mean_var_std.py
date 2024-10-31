import numpy as np

def check_array(check_list):

    if len(check_list) < 9:
        raise ValueError('List contains less than 9 elements')


def calculate(input_list):

    output_dict = {
        'mean' : [],
        'variance' : [],
        'standard deviation' : [],
        'max' : [],
        'min' : [],
        'sum' : []
    }
    input_list = np.array(input_list).reshape(3, 3)

    output_dict['mean'] = input_list.mean(axis=1).tolist(), input_list.mean(axis=0).tolist(), float(input_list.flatten().mean())
    output_dict['variance'] = input_list.var(axis=1).tolist(), input_list.var(axis=0).tolist(), float(input_list.flatten().var())
    output_dict['standard deviation'] = input_list.std(axis=1).tolist(), input_list.std(axis=0).tolist(), float(input_list.flatten().std())
    output_dict['max'] = input_list.max(axis=1).tolist(), input_list.max(axis=0).tolist(), int(input_list.flatten().max())
    output_dict['min'] = input_list.min(axis=1).tolist(), input_list.min(axis=0).tolist(), int(input_list.flatten().min())
    output_dict['sum'] = input_list.sum(axis=1).tolist(), input_list.sum(axis=0).tolist(), int(input_list.flatten().sum())

    display(output_dict)

def display(d_dict):

    for key, value in d_dict.items():
        print(f'{key} : {value}')

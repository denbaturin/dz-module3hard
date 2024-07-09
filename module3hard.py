def calculate_structure_sum(*data_):
    sum_ = 0
    for i in data_:
        if type(i) is str:
            sum_ += len(i)
        elif type(i) is list:
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif type(i) is tuple:
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif type(i) is set:
            for j in i:
                sum_ += calculate_structure_sum(j)
        elif type(i) is dict:
            for key, value in i.items():
                sum_ += calculate_structure_sum(key, value)
        elif type(i) is int:
            sum_ += i
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
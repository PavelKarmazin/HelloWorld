import random

def random_list(length, limit, series):
    List = []
    if type(length) != int or type(limit) != int or type(series) != int:
        return("Не корректные данные")
    elif length < 0 or limit < 0 or series < 0:
        return("Не корректные данные")
    
    for i in range(length):
        v = random.randint(0, limit)
        if len(List) == length:
            continue
        for ser in range(random.randint(0, series)):
            List.append(v)
            if len(List) == length:
                break

    return List

print(random_list(50, 100, 7))
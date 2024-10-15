def enumerate_list(strings):
    result = []
    count = 0  
    for index, color in enumerate(strings):
        if color:  # Solo toma los valores que no están vacíos
            result.append(f"{count}. {color}")
            count += 1  # Incrementa el contador solo para los strings no vacíos
    return result







def enumerate_backwards(list):
    result = []
    count = 0
    for index, value in enumerate(list):
        if value:  #Solo toma los valores que no estan vacios 
            result.append(f"{count}. {value[::-1]}")
            count += 1
    return result

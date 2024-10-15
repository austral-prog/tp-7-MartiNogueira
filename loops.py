def index_of_by_index(word, list, i):

    if i < 0 or i >= len(list):
        return -1
    
    for i in range(i, len(list)):
        if list[i] == word:
            return i  
            
    return -1 





def index_of_empty(list):


    for i, element in enumerate(list):
        if element == "":
            return i
    return -1



def index_of(word, list):

    if word in list:
        return list.index(word)
    else:
        return -1 


def put(color, list1):
    for i in range(len(list1)):
        if list1[i] == "":  
            list1[i] = color  
            return i  
    return -1  




def remove(word, list):
    count = 0
    for i in range(len(list)):
        if list[i] == word:
            list[i] = ""  
            count += 1   
    return count 








# You are given a dictionary aDict that maps integer keys to integer values. Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict.

# This function takes in a dictionary and returns a list.
# Return the list of keys in increasing order.
# If aDict does not contain any values appearing exactly once, return an empty list.
# If aDict is empty, return an empty list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    reverseDic = {}
    
    for key in aDict:
        if reverseDic.get(aDict[key],None) == None:
            reverseDic[aDict[key]] = key
        else:
            reverseDic[aDict[key]] = "duplicated"
            
    result = []
    for i in reverseDic:
        if reverseDic[i] != "duplicated":
            result.append(reverseDic[i])
    
    return sorted(result)
    
    

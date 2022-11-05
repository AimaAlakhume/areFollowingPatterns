def solution(strings, patterns):
    
    matchDict = {}
    
    if len(strings) != len(patterns):
        return False
        
    for i in range(len(strings)):
        if patterns[i] not in matchDict:
            if strings[i] not in matchDict.values():
                matchDict[patterns[i]] = strings[i]
            else: #if the string is already in the dict with a different value
                return False
        else: #if the pattern is in the dictionary
            if matchDict[patterns[i]] != strings[i]:
                #if there's a different key from the precedent set
                return False
    
    return True

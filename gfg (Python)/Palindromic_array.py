def isPalinArray(arr):
    # Code here
    s = [str(i) for i in arr]
    
    for i in s:
        if i != i[::-1]:
            return False
            break
    return True
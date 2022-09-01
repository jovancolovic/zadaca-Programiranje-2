l = [1,2,4,6]
def recursive(l):
    if len(l) == 0:
        return []
    else:
        return[l.pop()] + recursive(l)

print recursive(l)

def listSearch(L, x):
    """ Searches through a list L for the element x"""
    for item in L:
        if item == x:
            return True    # We found it, so return True
    return False           # Item not found
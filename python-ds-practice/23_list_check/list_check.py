def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    ret = True
    for item in lst:
        if not isinstance(item,list):
            ret = False
    return ret

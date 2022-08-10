def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_reverse = to_swap.swapcase()
    ret_str = ""
    for char in phrase:
        if char == to_swap or char == to_swap_reverse:
            ret_str += char.swapcase()
        else:
            ret_str += char
    return ret_str
print(flip_case('Aaaahhh', 'h'))
print(flip_case('Aaaahhh', 'A'))
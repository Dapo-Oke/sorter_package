def top_n(items, n):
    """
    Returns the top n numbers in an array in desc order.

    Args:
        items(array): list or array like object.
        n(int): number of items to return

    Return:
        array: top n items in desc order.

    Example:
        >>> top_n([8,3,3,7,4,1], 3)
        [8,7,4]
    """

    for i in range(n):
        for j in range(len(items)-1-i): #keep sorting until we have the top n items

            if items[j] > items[j+1]: #if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j] #swap the two

    #get the last two items
    top_n = items[-n:]

    #return in descending order
    return top_n[::-1]
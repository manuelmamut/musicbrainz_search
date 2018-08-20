def getYear(year):
    """
    Function used to check if the year is a valid date
    :param year: The year to compare
    :return year: the year or 0
    """

    if year == "":
        return 0
    return year[:4]


def getPaginationInfo(offset, limit, count):
    """
    Function used to return the pagination variables depending on the 
    offset, limit and count of objects to paginate
    :param offset: where star counting
    :param limit: where to stop counting
    :param count: count to compare if we must return a new offset
    :return next_offset: Where the next page should begin
    :return showing: from where to where are we showing elements
    """
    
    if (offset + limit) > count:
        showing = (offset, count)
        if offset > count:
            showing = "{}-{}".format(0,0)
        next_offset = 0
        return next_offset, showing

    next_offset = offset + limit
    showing = "{}-{}".format(offset, next_offset - 1)
    return next_offset, showing


def getYear(year):
    """
    Function used to check if the year is a valid date
    :param year: The year to compare
    :return year: the year or 0
    """

    if year == "":
        return 0
    return year[:4]

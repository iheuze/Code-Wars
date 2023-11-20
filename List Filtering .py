def filter_list(lst):
    return [element for element in lst if isinstance(element, int) and element >= 0]

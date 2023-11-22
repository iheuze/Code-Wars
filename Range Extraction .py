from itertools import groupby

def group_consecutives(lst):
    for _, g in groupby(enumerate(lst), lambda i_x: i_x[0] - i_x[1]):
        r = [x for _, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)

def solution(lst):
    return ','.join(group_consecutives(lst))

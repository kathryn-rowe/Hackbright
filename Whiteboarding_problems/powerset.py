def powerset(lst):
    result = [[]]

    for x in lst:
        result.extend([subset + [x] for subset in result])
    print result


lst = ['a', 'b', 'c', 'd']
powerset(lst)


def powersetlist(s):
    r = [[]]
    for e in s:
        r += [x+[e] for x in r]
    print r

s = ['a', 'b', 'c', 'd']
powersetlist(s)

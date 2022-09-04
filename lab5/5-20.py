def compact(src):
    if len(src) == 0:
        return ''
    if len(src) == 1:
        return src +'1'

    prev = src[0]
    count = 1
    form = ''

    for i in range(1, len(src)):
        new_prev = src[i]
        if prev == new_prev:
            count +=1

        else:
            form = form + prev + str(count)
            prev = new_prev
            count = 1

    return form + prev + str(count)


src = 'aaaabbb'
print("src='{}'".format(src))
print("output='{}'".format(compact(src)))
src = 'aaaabccccaaaaacccfg'
print("src='{}'".format(src))
print("output='{}'".format(compact(src)))

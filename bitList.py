def bitListA(x, y):
    output = []
    assert isinstance(x, int) and isinstance(y, int), "not integer"
    assert x>0 and y>0, "number is not positive"
    assert x < y, "the input should be switched"
    if x == 1:
        output.append(2)
    else:
        output.append(4*(2**(x-2)))
    for i in range(x+1, y+1):
        output.append(3*(2**(i-2)))
        output.append(4*(2**(i-2)))
    return output

def bitListB(x, y):
    output = []
    assert isinstance(x, int) and isinstance(y, int), "not integer"
    assert x>0 and y>0, "number is not positive"
    assert x < y, "the input should be switched"
    if x == 1:
        output.append(2)
        output.append(3)
        output.append(4)
    elif x == 2:
        output.append(4)
    else:
        output.append(8*(2**(x-3)))
    if x != 1:
        for i in range(x+1, y+1):
            output.append(5*(2**(i-3)))
            output.append(6*(2**(i-3)))
            output.append(7*(2**(i-3)))
            output.append(8*(2**(i-3)))
    else:
        for i in range(3, y+1):
            output.append(5*(2**(i-3)))
            output.append(6*(2**(i-3)))
            output.append(7*(2**(i-3)))
            output.append(8*(2**(i-3)))
    return output

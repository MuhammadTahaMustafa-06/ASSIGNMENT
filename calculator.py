def Calculator(a,b,oper):
    if oper=='+':
        return a+b
    elif oper=="-":
        return a-b
    elif oper=="*":
        return float(a)*b
    elif oper=="/":
        return float(a)/float(b)
print(Calculator(5,6,"/"))
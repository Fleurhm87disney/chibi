from exp import Val, Add

def parse(s: str):
    pos = s. find('+') #'+'記号を探す
    if pos == -1:
        return Val(int(s))
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1), parse(s2))

e = parse("1+2+3")
print(e, e.eval())

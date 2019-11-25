import pegpy

peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Value #Mul})*
Value = { [0-9]+ #Int }
''')
parser =  pegpy.generate(peg)

def calc(t):
    if t == 'Int':
        return int(str(t))
    if t == 'Add':
        return calc(t[0]) * calc(t[1])
    print(f'TODO {t.tag}')
    return 0 

t = parser('1+2*3')
print(repr(t))

t = parser('@2')
print(repr(t))

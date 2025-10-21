#local identifiers:

def display(name):
    age = 22
    x = 20
    print(f"{name} has age{age}")
    variables = locals()
    print(variables)
    print(variables['x'])
    #print(len(locals()))
    print(age)
    
display("rash")
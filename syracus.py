
def syracuse(u):

    while (u != 1):
        if (u % 2 == 0 and u > 0):

            u = u//2
            print(u)
        elif (u % 2 == 1 and u > 0):

            u = 3*u + 1    
            print(u)
        
    return u
print('veuillez insérer un entier > 0 :')
f = syracuse(int(input()))

def guess_age():
    inp = input("Greetings, I will try to guess your age. Please, type your name: ")
    for i in range(15, 31):
        inpu = input("Are you " + str(i) + "? - ")
        if inpu == 'y':
            print(inp + " is " + str(i))
            return
        elif inpu == 'n':
            print("Rats")
    return
guess_age()
        
        
        
        
    

        
        
        
        
    
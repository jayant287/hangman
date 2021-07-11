from random import choice
def random_generate():
    with open("words.txt","r") as f:
        lines=f.readlines()
    f.close()
    lines=[i.strip("\n") for i in lines]
    return choice(lines)
name = input("What is your name? \n")
print("Hello, " + name, "Lets play hangman!")
print("Start guessing...")
word = random_generate()
guesses = ""
turns = len(word)+3
while turns > 0:         
    fail = 0             
    for char in word:      
        if char in guesses:    
            print (char,end=" ")   

        else:
            print ("_",end=" ")     
            fail += 1    
    if fail == 0:
        print("\n")        
        print ("Congratulations You  have won !!!!!")
        print("The word is:",word)
        break              
    guess = input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1
        print("Wrong")
        print("You have more "+str(turns)+" turns remaining" ) 
        if turns == 0:           
            print("You have lost")
            print("The word was: ",word)
            print("Better luck next time")
 

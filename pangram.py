class Solution:                           
    frase = input("introduce frase: ") 
    def Pangram(frase):                  
       if len(set(frase)) == 26:          #set para eliminar duplicados, 26 == numero de letras diferentes
            print("True")
       else:
            print("False")
    Pangram(frase)
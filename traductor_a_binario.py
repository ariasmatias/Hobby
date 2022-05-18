def morse():    
    dicc={ 
        "A":".-", "B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
        "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
        "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
        "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."," ":" " } 
    



    texto= input("Ingrese una palabra:").upper()
    print("Traduccion a Clave Morse: ",end=" ")
    for element in texto:
        key=dicc[element]
        print(key,end=' ')
    

        
morse()
        



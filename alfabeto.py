def alfabeto(letra):
    vogal = ['A', 'E', 'I', 'O', 'U']
    
    if letra.upper() in vogal:
        print(letra, "É uma vogal")
    else:
        print(letra, "É uma consoante")


letra = input("DIgite uma letra: ")
alfabeto(letra)
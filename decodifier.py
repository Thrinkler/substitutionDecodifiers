

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

#for _ in abecedario[0]:  #hace una matriz de abecedario
 #   new = abecedario[-1].copy()
  #  new.append(new[0])
   ##abecedario.append(new)


mensaje = input("dame el mensaje ")
key = input("dame la llave para el mensaje ")

longest = mensaje
shortest = key
if len(longest) < len(shortest):
    longest = key
    shortest = mensaje

coded = ""
decoded = ""
for ind,messajeletter in enumerate(mensaje):
    keyletter = key[ind%len(key)]
    x = 99
    y = 99
    for i,l in enumerate(abecedario): ### ooooooooooooo aqui para el decodificador tradicional, poner en vez de abecedario 0, poner abecedario Y y el decoded abecedario 0,X

        if keyletter == l:
            y = i
        if messajeletter == l:
            x = i
    Ei = (x + y)%(len(abecedario)+1)
    Di = (x - y+ len(abecedario)+1)%(len(abecedario)+1)
    if x == 99 or y == 99:
        coded = coded+ messajeletter
        decoded = decoded + messajeletter
    else:
        #coded = coded+ abecedario[y][x]
        coded = coded+ abecedario[Ei]
        decoded = decoded + abecedario[Di]




print(coded)
print(decoded)

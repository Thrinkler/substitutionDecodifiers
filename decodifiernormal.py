abecedario = [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]]

for _ in abecedario[0]:  #hace una matriz de abecedario
    new = abecedario[-1].copy()
    new.append(new[0])
    new.pop(0)
    abecedario.append(new)

mensaje = input("dame el mensaje ")
key = input("dame la llave para el mensaje ")


def coding(mensaje,key,abecedario):
    coded = ""
    for ind,messajeletter in enumerate(mensaje):
        keyletter = key[ind%len(key)]
        x = 99
        y = 99
        for i,l in enumerate(abecedario[0]): # aqui para el decodificador tradicional, poner en vez de abecedario 0, poner abecedario Y y el decoded abecedario 0,X
            if keyletter == l:
                y = i
            if messajeletter == l:
                x = i
        if x == 99 or y == 99:
            coded = coded+ messajeletter
        else:
            coded = coded+ abecedario[y][x]
    return(coded)

def decoding(code,key,abecedario):
    mensaje = code

    decoded = ""
    for ind,messajeletter in enumerate(mensaje):
        keyletter = key[ind%len(key)]
        x = 99
        y = 99
        for i,l in enumerate(abecedario[0]):
            if keyletter == l:
                y = i
                break
        for i,l in enumerate(abecedario[y]):
            if messajeletter == l:
                x = i
                break
        if x == 99 or y == 99:
            decoded = decoded+ messajeletter
        else:
            decoded = decoded+ abecedario[0][x]
    return(decoded)

code = coding(mensaje,key,abecedario)

print(code)
print(decoding(code,key,abecedario))


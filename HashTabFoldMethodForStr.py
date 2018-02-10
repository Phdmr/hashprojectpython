import textwrap
key = None
upi = 0
lenhas = 11
has = [None for i in range(lenhas)]
print(has)
lista = ['amor', 'gato', 'numb', 'mute', 'vrau', "marituba"]
for f in range(len(lista)):
    x = ""
    vt = []
    teste = list(lista[f])
    for lp in range(len(teste)):
        vt.append(str(ord(teste[lp])))
    for j in range(len(vt)):
        x = x + vt[j]
    print("Valor de x: ", x)
    inp = textwrap.wrap(x, 2)
    for h in range(len(inp)):
        upi += int(inp[h])
    inp = upi
    print("Valor bruto: ", inp)
    k = inp % lenhas
    print("Chave %s para %s: " % (k, lista[f]))
    if has[k] is None:
        has[k] = lista[f]
    else:
        for t in range(k+1, lenhas):
            if has[t] is None:
                has[t] = lista[f]
                break
            if t == lenhas and has[k] is not None:
                for c in range(lenhas):
                    if has[t] is None:
                        has[t] = lista[f]
                        break
    print(has)


print(has)
for jk in range(lenhas):
    if has[jk] is not None:
        print("Chave: %s\nElemento: %s" % (jk, has[jk]))
input("Aperte Enter para finalizar")

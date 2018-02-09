import textwrap
x = ""
vt = []
key = None
upi = 0
lenhas = 11
has = [None for i in range(lenhas)]
print(has)
lista = ['if', 'you', 'seek', 'amy', 'tonight']
for f in range(len(lista)):
    teste = list(lista[f])
    for lp in range(len(teste)):
        vt.append(str(ord(teste[lp])))
    for j in range(len(vt)):
        x = x + vt[j]
    x = str(int(x)**2)
    inp = textwrap.wrap(x, 1)
    if len(inp) % 2 == 0:
        firstpart, secondpart = inp[:len(inp) // 2], inp[len(inp) // 2:]
        upi = firstpart[-1] + secondpart[0]
    if len(inp) % 2 != 0:
        firstpart, secondpart = inp[:len(inp) // 2], inp[len(inp) // 2:]
        upi = secondpart[0] + secondpart[1]
    inp = int(upi)
    print("Valor bruto: ", inp)
    k = inp % lenhas
    print("Chave %s para %s: " % (k, lista[f]))
    if has[k] is None:
        has[k] = lista[f]
    else:
        for t in range(lenhas):
            if has[t] is None:
                has[t] = lista[f]
                break
print(has)
for jk in range(lenhas):
    if has[jk] is not None:
        print("Chave: %s\nElemento: %s" % (jk, has[jk]))

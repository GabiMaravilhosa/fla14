n = 0
otimo =0
bom = 0
regular =0
p =0
ida = 0
while n < 3:
    i = int(input("digite a sua idade: "))
    o = input ("digite a sua nota: (3 - otimo/ 2 - bom/ 1 - regular) ")
    if o == '3':
        otimo += 1
        ida = i + 1
        p += 1
    if o == '1':
        regular += 1
    if o == '2':
        bom += 1
    n += 1
a = ida / p
b = (3 * bom)/100
print(" media das idades que responderam ótimo: ", a)
print("quantidade que acharam regular: ", regular)
print("a porcentagem que acharam bom: ", b  )

texto = "X-DSPAM-Confidence:0.8475"
inicio = texto.find(":") + 1
final = len(texto)
final2 = texto.find(",")
numero = float(texto[inicio:final2])
print(inicio, final)
print(numero)
print(type(numero))
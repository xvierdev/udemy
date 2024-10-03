a = 'AAA'
b = 'BBBBB'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
formato2 = 'a={nome2} b={nome1} c={nome3:.2f}'.format(
    nome1 = a,  # Parâmetro nomeado
    nome2 = b,
    nome3 = c
)

print(formato)
print(formato2)
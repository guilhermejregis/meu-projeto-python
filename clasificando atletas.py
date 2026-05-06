ano=int(input('Digite o ano do seu nascimento:'))
cat=2026-ano
if cat<=9:
    print('Sua categoria é mirim')
elif cat<=14 and cat>9:
    print('Sua categoria é infantil.')
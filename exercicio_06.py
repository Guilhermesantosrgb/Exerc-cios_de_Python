idade= int(input('Informe sua idade:'))
print(idade, 'anos')
if idade < 16:
    print('Nao pode votar')
elif idade > 65:
    print('voto opcional')
elif idade == 16:
    print('voto opcional')
elif idade == 17:
    print('voto opcional')

else:
    print('Voto obrigatorio')
print('Vamos supor que voce tenha 5 notas no bimestre, digite elas')
nota1=float(input('primeira:'))
print(nota1)
nota2=float(input('segunda:'))
print(nota2)
nota3=float(input('terceira:'))
print(nota3)
nota4=float(input('quarta:'))
print(nota4)
nota5=float(input('quinta:'))
print(nota5)
media= (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('Sua media e:', media)
if media > 6:
    print('aprovado(a)')
else:
    print('reprovado(a)')
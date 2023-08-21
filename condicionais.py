
### Solicitar o nome do aluno, 2 notas e calcular a média
# (nota1 + nota2) / 2

# retornar se o aluno foi aprovado ou não

nome = input("Insira seu nome : ")
nota1 = int(input("Nota 1 : ")) 
nota2 = int(input("Nota 2 : "))
media = (nota1 + nota2) / 2
print(f"O aluno {nome} teve média {media:.2f}")

if media >= 7 :
    print("O aluno foi Aprovado!")
elif media >= 5 :
    print("O aluno está de recuperação!!")
else:
    print("O aluno foi reprovado :(")
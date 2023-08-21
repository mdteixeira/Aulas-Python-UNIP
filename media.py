### Solicitar o nome do aluno, 2 notas e calcular a média
# (nota1 + nota2) / 2

nome = input("Insira seu nome : ")
nota1 = int(input("Nota 1 :")) 
nota2 = int(input("Nota 2 : "))
media = (nota1 + nota2) / 2
print(f"O aluno {nome} teve média {media:.2f}")
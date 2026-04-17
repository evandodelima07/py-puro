#Variáveis e Entrada de Dados



#3.1/2 - Nomeação de variáveis e variáveis do tipo numéricas



idade = 20
_b = -10
print(_b)

var90 = 0.1
salário_médio = 2000.0
print(3 * var90)



#3.3 - Variáveis do tipo lógicas



var = True
a1 = False

a = 1
b = 5.0
c = 5
d = 1

print(c == b)
print(d != a)
print(b > a)
print(b < a)
print(b >= a)
print(b <= a)

nota = 8
media = 7
aprovado = nota >= media
print(aprovado)

print(not True)
print(not False)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(salário_médio > 1000 and idade > 18)
print(False and True)

'''3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não 
pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que 
R$ 1.200,00.'''

criterio_salario_imposto = 1200.0

salario_cidadao = float(input("Digite o salário: "))

pagar_imposto = salario_cidadao > criterio_salario_imposto

if pagar_imposto:
    print("O cidadão deve pagar imposto.")
else:
    print("O cidadão não deve pagar imposto.")


'''Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi 
ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores 
que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma 
está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.'''

materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))

media_aprovacao = 7.0

aprovado = (materia1 > media_aprovacao) and (materia2 > media_aprovacao) and (materia3 > media_aprovacao)

if aprovado == True:
    print("O aluno foi aprovado.")
else:
    print("O aluno não foi aprovado.")



#3.4 Variáveis do tipo string



nome = "Maria"

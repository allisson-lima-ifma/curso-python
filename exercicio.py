# 1. Conversão de Tipos

print("Exercício 1:")
numero_inteiro = int("123")
print(numero_inteiro)

numero_float = float(numero_inteiro)
print(numero_float)

print("\n-------------------------\n")

# 2. Operações com Strings

print("Exercício 2:")
texto = "Python é incrível!"
print(len(texto))               # Conta os caracteres
print(texto.upper())           # Converte para maiúsculas
print(texto.replace("incrível", "poderoso"))  # Substitui palavras

print("\n-------------------------\n")

# 3. Listas e Indexação

print("Exercício 3:")
numeros = [10, 20, 30, 40, 50]
print(numeros[2])              # Terceiro elemento (índice 2)
numeros.append(60)            # Adiciona 60 no final
numeros.remove(20)            # Remove o número 20
print(numeros)

print("\n-------------------------\n")

# 4. Dicionários

print("Exercício 4:")
aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Engenharia"
}
aluno["notas"] = [8.5, 7.0, 9.2]
print(aluno["curso"])

print("\n-------------------------\n")

# 5. Tuplas e Conjuntos

print("Exercício 5:")
cores = ("vermelho", "verde", "azul", "verde")
cores_unicas = set(cores)
cores_unicas.add("amarelo")
print(cores_unicas)

print("\n-------------------------\n")

# 6. Operações Matemáticas

print("Exercício 6:")
a = 15
b = 4
print(a // b)     # Divisão inteira
print(a % b)      # Resto da divisão

print("\n-------------------------\n")

# 7. Verificação de Tipos

print("Exercício 7:")
dados = [42, 3.14, "Python", True, [1, 2]]
for item in dados:
    print(type(item))

print("\n-------------------------\n")

# 8. Manipulação de Strings

print("Exercício 8:")
texto = "programação"
invertida = texto[::-1]
print(invertida)
print(texto == invertida)

print("\n-------------------------\n")

# 9. Listas Aninhadas

print("Exercício 9:")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][1])           # Número 5
matriz[2][1] = 10             # Substitui 8 por 10
print(matriz)

print("\n-------------------------\n")

# 10. Desafio Final

print("Exercício 10:")
estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}
estoque["pera"] = 12          # Adiciona "pera"
del estoque["banana"]         # Remove "banana"
print(estoque.keys())         # Imprime as chaves

print("\n-------------------------\n")

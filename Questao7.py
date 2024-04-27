# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

usuario = input("Seu nome: ")
idade = int(input("Sua idade: "))
final = input("Seu email: ")

cadastro = { "nome": usuario , "idade": idade , "email": final}
print(cadastro["nome"])
print(cadastro["idade"])
print(cadastro["email"])

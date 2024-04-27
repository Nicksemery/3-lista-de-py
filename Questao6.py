# Seja criativo ao desenvolver este programa.
        #a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
        #b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
        #c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
        #d. Modifique sua lista, substitua os desistentes por novos convidados.
        #e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

lista = ["Emma Stone", "Tom Hardy", "Adrien Brody", "Bryan Cranston", "Aaron Pinkman"]
for convite in lista:
    print ("\n" f"O Podrão do Neto convida {convite} para um jantar particular no Bairro Dos Estados ")

print("\n"f"Como {lista[3]} e {lista[4]} não virão")

lista[3] = "Hozier"
lista[4] = "Dave Grohl"
print("\n"f"{lista[3]} e {lista[4]} estão convidados no loca dos desistentes.")

for novo in lista:
    print ("\n"f"{novo} confirmou a presença")
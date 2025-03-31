import os
os.system("clear")

print("Restaurante Gourmet Tech\n")

print("Confira nosso cardapio: ")

soma = 0
contador = 0
quantidade = 0
valor = 0
desconto = 0
subtotal = 0
acrescimo = 0
total = 0




  
while True:

    opcao = int(input("""
    Codigo  \t\t Prato \t\t\t valor
        1   \t\t Picanha \t\t R$ 25,00
        2   \t\t Lasanha \t\t R$ 20,00
        3   \t\t Strogonoff \t\t R$ 18,00
        4   \t\t Bife acebolado \t R$ 15,00
        5   \t\t Pão com ovo \t\t R$ 5,00
        6   \t\t Refrigerante \t\t R$ 6.00
        7  \t\t  Suco \t\t\t R$ 2.50
                    
    Digite a opção desejada: """))

    match opcao:

       case 1:

         print("Prato escolhido: Picanha")
         valor: 25.00

       case 2:

         print("Prato escolhido: Lasanha")

         valor: 20.00

       case 3:

        print("Prato escolhido: Strogonoff")

        valor: 18.00

       case 4:

        
        print("Prato escolhido: Bife acebolado")

        valor: 15.00

       case 5:
        
         print("Prato escolhido: Pão com ovo")

         valor: 5.00

       case 6:
        
         print("Prato escolhido: Refrigerante")

         valor: 6.00

       case 7:
        
         print("Prato escolhido: Suco")

         valor: 2.50

       case _:


        print("Codigo invalido, insira um codigo novamente")


        opcao = int(input("""
        Codigo  \t\t Prato \t\t\t valor
            1   \t\t Picanha \t\t R$ 25,00
            2   \t\t Lasanha \t\t R$ 20,00
            3   \t\t Strogonoff \t\t R$ 18,00
            4   \t\t Bife acebolado \t R$ 15,00
            5   \t\t Pão com ovo \t\t R$ 5,00
            6   \t\t Refrigerante \t\t R$ 6.00
            7  \t\t  Suco \t\t R$ 2.50
                        
        Digite a opção desejada: """))




    quantidade = input("Deseja fazer outro pedido? (S ou N)").upper()

    if quantidade == "N":
      
      break

    else:
     
     quantidade = int(input("Digite o outro pedido: "))


     contador += 1

     soma += opcao




     if opcao == 0:

        valor * 0.10

        print(f"Valor total a pagar é {valor}")

        break
     
    pagamento = int(input(""""
    forma de pagamento\t\tdesconto
        1\t\t Á vista\t\t 10 por cento de desconto
        2\t\t Cartão de credito\t\t acréscimo de 10 por cento

                           Digite a forma de pagamento:"""))
    

    if pagamento == 1:

        print("Certo, calculando valor")


    else:
        print("Certo, calculando valor")



    
    match pagamento:

        case 1:
           
           valor * 0.10
           
           if opcao == 1:
             
             subtotal = valor
             desconto = valor - 0.10
             total = valor + contador

             print(f"Prato escolhido: {opcao} Picanha")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")

           elif opcao == 2:
             
             subtotal = valor
             desconto = valor - 0.10
             total = valor + contador

             print(f"Prato escolhido: {opcao} Lasanha")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


           elif opcao == 3:
             
             subtotal = valor
             desconto = valor - 0.10
             total = valor + contador

             print(f"Prato escolhido: {opcao} Strogonoff")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


            elif opcao == 4:
             
              subtotal = valor
              desconto = valor - 0.10
              total = valor + contador

             print(f"Prato escolhido: {opcao} Bife acebolado")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


            elif opcao == 5:
             
             subtotal = valor
             desconto = valor - 0.10
             total = valor + contador

             print(f"Prato escolhido: {opcao} Pão com ovo")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


            elif opcao == 6:
             
               subtotal = valor
               desconto = valor - 0.10
               total = valor + contador

             print(f"Prato escolhido: {opcao} Refrigerante")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


            elif opcao == 7:
             
             subtotal = valor
             desconto = valor - 0.10
             total = valor + contador

             print(f"Prato escolhido: {opcao} Suco")
             print(f"o subtotal a pagar é: {subtotal}")
             print(f"A forma de pagamento escolhida foi: {pagamento}")
             print(f"o valor do desconto foi de: {desconto} ")
             print(f"O valor total a pagar é: {total}")


           


        


        
        


        
           
        
      




        








    



      

        

       


  

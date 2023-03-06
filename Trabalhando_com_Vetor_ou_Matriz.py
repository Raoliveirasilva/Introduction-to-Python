"""  Escrever um algoritmo que lê: 

- a porcentagem do IPI a ser acrescido no valor das peças 

- o código da peça 1, valor unitário da peça 1, quantidade de peças 1 

- o código da peça 2, valor unitário da peça 2, quantidade de peças 2 



O algoritmo deve calcular o valor total a ser pago e apresentar o resultado. 

Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1) """

# Adicionando informações da porcentagem do IPI
ipi = float(input('Informe a porcentagem do IPI a ser acrescido: '))

# Informações da peça 1
cod1 = int(input('informe aqui o codigo da peça 1: '))
valor_unit1 = float(input('Informe aqui o valor unitario da peça 1: '))
quant1 = int(input('Informe aqui a quantidade de peças 1: '))

# Informações da peça 2
cod2 = int(input('informe aqui o codigo da peça 2: '))
valor_unit2 = float(input('Informe aqui o valor unitario da peça 2: '))
quant2 = int(input('Informe aqui a quantidade de peças 2: '))

# calculo do valor total a pagar
subtotal1 = valor_unit1 * quant1
subtotal2 = valor_unit2 * quant2
subtotal = subtotal1 + subtotal2
total = subtotal * (1 + ipi/100)

# Resultado final
print("Valor total a ser pago: R$", total)
from utilidadescev import moeda, dado
p = dado.leiaDinheiro('Digite um preço: ')
aumento = float(input('Quanto por cento (%) de aumento você quer? '))
diminuicao = float(input('Quanto por cento (%) de redução você quer? '))
moeda.resumo(p, aumento, diminuicao)
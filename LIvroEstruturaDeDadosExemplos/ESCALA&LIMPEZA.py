#Regras para criar a escala da semana de uma empresa pequena real
#referente aos horarios de almoco e turnos de limpeza 
#
############################escala#############################
#se folgar no domingo, não folga na semana
#há três horários de almoço: 11h30, 12h30, 13h30
#no dia que a Jane folga a tarde, o horário de almoço dela é o último
#
############################limpeza############################
#se lavar a loja de cima, nao lava a de baixo

#Em construcao
    #por enquanto a primeira versao vai ser no terminal
    #mas logo farei uma versao em java com tela e campos de input apropriados
    #por ora, focarei no algoritmo
    #
    #inserir os funcionarios
    #inserir quem folga no domingo
    #inserir se a Jane vai folgar
nomeFuncionarios = input()
nomeDeQuemFolgaNoDomingo = input()
print("Jane folga a tarde? Escreva S para sim e N para não.")
janeFolgaATarde = input()
while ((janeFolgaATarde != "S") or (janeFolgaATarde != "N")) :
    print("Cara, escreve só S ou N, por favor.")
    janeFolgaATarde = input()

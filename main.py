from random import randint

lista_npcs = []

player = {
    "nome": "Vinicius",
    "level": 1,
    "exp":  0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25 
}

def criar_npcs(level):

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }

    return novo_npc

def gerar_npcs(n_npcs):
    for x in range (n_npcs):
        novo_npc = criar_npcs(x + 1)
        lista_npcs.append(novo_npc)


def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc
        

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // level: {npc['level']} // dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}.")



def exibir_player():
    print(f"Nome: {player['nome']} // level: {player['level']} // dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}.")

def reset_player():
     player['hp'] = player['hp_max']

def reset_npc(npc):
     npc['hp'] = npc['hp_max']     

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp'] += 20
         


def iniciar_batalha(npc):
            while player['hp'] > 0 and npc['hp'] > 0:
                atacar_npc(npc)
                atacar_player(npc)
                exibir_infobatalha(npc)

            if player ['hp'] > 0:            
                print(f"O player {player['nome']}, ganhou e venceu {npc['exp']} de experiencia, agora o player tem de EXP !")
                player['exp'] += npc['exp']
                exibir_player()
            else:
                print(f"O player {npc['nome']}, venceu!")
                exibir_npc(npc)
                

            level_up()
            reset_player()
            reset_npc(npc)
                

def atacar_npc(npc):
    npc['hp'] -= player['dano']

def atacar_player(npc):
    player['hp'] -= npc['dano']

def exibir_infobatalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']} {npc['hp']}/{npc['hp_max']}")
    print("--------------\n")


gerar_npcs(5)
#exibir_npcs()

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
exibir_player()

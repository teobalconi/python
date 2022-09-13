entrada = ""
tarefas = []
tarefas_del = []


def listar(lista_tarefas):
    print("")
    if lista_tarefas:
        for i, t in enumerate(lista_tarefas):
            print(f"Tarefa {i + 1}: {t}")
    else:
        print("Lista de TAREFAS vazia!")


def desfazer(lista_tarefas, lista_tarefas_del):
    if not lista_tarefas:
        print("Não há tarefas para DESFAZER!")
    else:
        lista_tarefas_del.append(lista_tarefas[-1])
        lista_tarefas.pop()
    return


def refazer(lista_tarefas, lista_tarefas_del):
    if not lista_tarefas_del:
        print("Não há tarefas para REFAZER!")
    else:
        lista_tarefas.append(lista_tarefas_del[-1])
        lista_tarefas_del.pop()
    return


def deletar(lista_tarefas):
    lista_tarefas.pop()


while True:
    entrada = input("\nDigite a nova TAREFA. \nDemais opções: LISTAR, DESFAZER, REFAZER, DELETAR ou SAIR! \n")
    vazio = entrada == ""

    if entrada.lower() == "sair":
        break

    elif entrada.lower() == "listar":
        listar(tarefas)

    elif entrada.lower() == "refazer":
        refazer(tarefas, tarefas_del)

    elif entrada.lower() == "desfazer":
        desfazer(tarefas, tarefas_del)

    elif entrada.lower() == "deletar":
        deletar(tarefas)

    elif not vazio:
        tarefas.append(entrada)
        
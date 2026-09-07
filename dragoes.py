def classificar_idade(idade):
    if idade >= 100:
        return "Ancião"
    elif idade >= 50:
        return "Adulto"
    else:
        return "Jovem"


def habilidade_especial(elemento):
    habilidades = {
        "fogo": "respirar chamas",
        "água": "controlar água",
        "terra": "criar terremotos",
        "ar": "controlar ventos"
    }
    return habilidades.get(elemento.lower(), "sem habilidade especial")


def fraqueza(elemento):
    fraquezas = {
        "fogo": "água",
        "água": "terra",
        "terra": "ar",
        "ar": "fogo"
    }
    return fraquezas.get(elemento.lower(), "desconhecida")


def calcular_raridade(idade, elemento, cor):
    elemento = elemento.lower()
    cor = cor.lower()
    if idade > 150 and elemento.lower() == "fogo" and cor.lower() == "azul":
        return "Lendário"
    elif (elemento.lower() == "água" and cor.lower() == "prata") or (elemento.lower() == "terra" and cor.lower() == "verde"):
        return "Raro"
    else:
        return "Comum"


def cadastrar_dragao():
    nome = input("Nome do dragão: ")
    idade_texto = input("Idade do dragão: ")
    elemento = input("Elemento do dragão: ")
    cor = input("Cor do dragão: ")

    if idade_texto.isdigit():
        idade = int(idade_texto)
    else:
        idade = 0

    categoria = classificar_idade(idade)
    raridade = calcular_raridade(idade, elemento, cor)

    return {
        "nome": nome,
        "idade": idade,
        "elemento": elemento,
        "cor": cor,
        "categoria": categoria,
        "raridade": raridade,
        "habilidade": habilidade_especial(elemento),
        "fraqueza": fraqueza(elemento)
    }


def mostrar_dragao(dragao):
    print(f"\nNome: {dragao['nome']}")
    print(f"Idade: {dragao['idade']}")
    print(f"Categoria: {dragao['categoria']}")
    print(f"Elemento: {dragao['elemento']}")
    print(f"Cor: {dragao['cor']}")
    print(f"Habilidade especial: {dragao['habilidade']}")
    print(f"Fraqueza: {dragao['fraqueza']}")
    print(f"Raridade: {dragao['raridade']}")


def mostrar_bestiario(bestiario):
    if not bestiario:
        print("Nenhum dragão cadastrado ainda.")
        return

    print("\nBestiário:")
    for dragao in bestiario:
        print(f"- {dragao['nome']} | {dragao['categoria']} | {dragao['elemento']} | {dragao['raridade']}")


def buscar_dragao(bestiario):
    nome_busca = input("Digite o nome do dragão para buscar: ").strip().lower()
    encontrado = False

    for dragao in bestiario:
        if dragao["nome"].lower() == nome_busca:
            mostrar_dragao(dragao)
            encontrado = True
            break

    if not encontrado:
        print("Dragão não encontrado.")


def calcular_forca(dragao):
    forca = dragao["idade"]
    bonus_elemento = {"fogo": 25, "água": 20, "terra": 22, "ar": 18}
    forca += bonus_elemento.get(dragao["elemento"].lower(), 0)

    if dragao["raridade"] == "Lendário":
        forca += 50
    elif dragao["raridade"] == "Raro":
        forca += 25

    if dragao["categoria"] == "Ancião":
        forca += 20
    elif dragao["categoria"] == "Adulto":
        forca += 10

    return forca


def simular_batalha(bestiario):
    if len(bestiario) < 2:
        print("Cadastre pelo menos dois dragões para batalhar.")
        return

    print("\nDragões disponíveis:")
    for i, dragao in enumerate(bestiario, start=1):
        print(f"{i} - {dragao['nome']}")

    escolha1 = int(input("Escolha o primeiro dragão: ")) - 1
    escolha2 = int(input("Escolha o segundo dragão: ")) - 1

    dragao1 = bestiario[escolha1]
    dragao2 = bestiario[escolha2]

    forca1 = calcular_forca(dragao1)
    forca2 = calcular_forca(dragao2)

    print(f"\n{dragao1['nome']} tem força {forca1}")
    print(f"{dragao2['nome']} tem força {forca2}")

    if forca1 > forca2:
        print(f"{dragao1['nome']} venceu a batalha!")
    elif forca2 > forca1:
        print(f"{dragao2['nome']} venceu a batalha!")
    else:
        print("A batalha terminou em empate!")


bestiario = []

while True:
    print("\n===== MENU DO BESTIÁRIO =====")
    print("Digite o número da opção desejada:")
    print("1 - Cadastrar dragão")
    print("2 - Mostrar bestiário")
    print("3 - Buscar dragão pelo nome")
    print("4 - Simular batalha")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        dragao = cadastrar_dragao()
        bestiario.append(dragao)
        print("\nDragão cadastrado com sucesso!")
        mostrar_dragao(dragao)
    elif opcao == "2":
        mostrar_bestiario(bestiario)
    elif opcao == "3":
        buscar_dragao(bestiario)
    elif opcao == "4":
        simular_batalha(bestiario)
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
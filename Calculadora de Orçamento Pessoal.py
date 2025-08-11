# calculadora_orcamento.py
# Projeto: Calculadora de Orçamento Pessoal
# Autor: [Seu Nome]
# Data: 2025-08-11

despesas = []
entradas = []

def adicionar_despesa():
    descricao = input("Descrição da despesa: ")
    try:
        valor = float(input("Valor da despesa (R$): "))
    except ValueError:
        print("⚠ Valor inválido! Tente novamente.")
        return
    despesas.append({"descricao": descricao, "valor": valor})
    print("✅ Despesa adicionada com sucesso!")

def adicionar_entrada():
    descricao = input("Descrição da entrada: ")
    try:
        valor = float(input("Valor da entrada (R$): "))
    except ValueError:
        print("⚠ Valor inválido! Tente novamente.")
        return
    entradas.append({"descricao": descricao, "valor": valor})
    print("✅ Entrada adicionada com sucesso!")

def listar_despesas():
    if not despesas:
        print("Nenhuma despesa registrada.")
        return
    print("\n=== Lista de Despesas ===")
    for i, desp in enumerate(despesas, 1):
        print(f"{i}. {desp['descricao']} - R$ {desp['valor']:.2f}")
    print(f"Total de despesas: R$ {calcular_total_despesas():.2f}\n")

def listar_entradas():
    if not entradas:
        print("Nenhuma entrada registrada.")
        return
    print("\n=== Lista de Entradas ===")
    for i, ent in enumerate(entradas, 1):
        print(f"{i}. {ent['descricao']} + R$ {ent['valor']:.2f}")
    print(f"Total de entradas: R$ {calcular_total_entradas():.2f}\n")

def calcular_total_despesas():
    return sum(d["valor"] for d in despesas)

def calcular_total_entradas():
    return sum(e["valor"] for e in entradas)

def calcular_saldo():
    total_entradas = calcular_total_entradas()
    total_despesas = calcular_total_despesas()
    saldo = total_entradas - total_despesas

    print("\n=== Resumo Financeiro ===")
    print(f"Total de entradas: R$ {total_entradas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print(f"💰 Saldo final: R$ {saldo:.2f}")
    if saldo >= 0:
        print("✅ Você está no positivo!")
    else:
        print("⚠ Atenção! Você está no negativo.")

def menu():
    while True:
        print("\n--- Calculadora de Orçamento Pessoal ---")
        print("1. Adicionar despesa")
        print("2. Adicionar entrada")
        print("3. Listar despesas")
        print("4. Listar entradas")
        print("5. Calcular saldo final")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_despesa()
        elif opcao == "2":
            adicionar_entrada()
        elif opcao == "3":
            listar_despesas()
        elif opcao == "4":
            listar_entradas()
        elif opcao == "5":
            calcular_saldo()
        elif opcao == "6":
            print("Saindo... Obrigado por usar!")
            break
        else:
            print("⚠ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

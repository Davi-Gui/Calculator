from app import gui, operations

def main() -> None:
    calculator = operations.Calculator()

    menu: str = """
    Calculadora
    0 -> Sair
    1 -> Soma
    2 -> Subtração
    3 -> Multiplicação
    4 -> Divisão
    """

    while True:
        print(menu)
        choice: int = int(input("Sua escolha: "))

        if choice == 0:
            print("Saindo...")
            break

        num = float(input("Digite o número: "))

        match choice:
            case 1:
                calculator.add(num)
            case 2:
                calculator.subtract(num)
            case 3:
                calculator.multiply(num)
            case 4:
                calculator.divide(num)
            case _:
                print("Opção inválida, tente novamente.")
                continue

        print(f"Resultado atual: {calculator.get_result()}")

if __name__ == "__main__":
    main()
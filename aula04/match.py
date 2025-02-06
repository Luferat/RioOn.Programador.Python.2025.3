def operation(value):
    match value:
        case "a":
            return "Opção 1"
        case "b":
            return "Opção 2"
        case "c":
            return "Opção 3"
        case _:
            return "Opção inválida"

print(operation("b"))  # Saída: Opção 2
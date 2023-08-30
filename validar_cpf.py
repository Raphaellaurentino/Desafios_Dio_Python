def validar_cpf(cpf):
    # Remover caracteres especiais e espaços
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcular os dígitos verificadores
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0

    # Verificar se os dígitos verificadores correspondem
    return cpf[-2:] == f"{digito_1}{digito_2}"

# Exemplo de uso
cpf_digitado = input("Digite o CPF: ")
if validar_cpf(cpf_digitado):
    print("CPF válido!")
else:
    print("CPF inválido!")
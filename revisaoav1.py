def formatar_citacao(nome_completo):
  
    partes = nome_completo.split()

    sobrenome = partes[-1].upper()

    nomes = " ".join(partes[:-1])

    return sobrenome + ", " + nomes


def gerar_codigo(ano, cpf):

    cpf = cpf.strip()

    primeiros_digitos = cpf[:3]

    return "ALU-" + ano + "-" + primeiros_digitos

autor = "Carlos Eduardo Andrade"
citacao_formatada = formatar_citacao(autor)
print("Citacao Bibliografica:", citacao_formatada)

matricula = gerar_codigo("2026", "456.789.123-00")
print("Matricula Gerada     :", matricula)


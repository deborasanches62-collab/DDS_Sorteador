import random
from calendar import monthrange

# Lista de frases para o DDS
frases_dds = [
    "Use sempre o cinto de segurança ao dirigir.",
    "Mantenha sua estação de trabalho organizada para evitar acidentes.",
    "Nunca ignore os procedimentos de segurança com máquinas.",
    "Use equipamentos de proteção individual sempre que necessário.",
    "Fique atento aos riscos de queda em locais altos.",
    "A segurança não acontece por acaso, acontece por sua atitude.",
    "Pare, pense e pratique a segurança.",
    "A pressa é inimiga da segurança.",
    "Não confie na sorte, foque na sua segurança.",
    "A prevenção é a melhor demonstração de amor próprio no trabalho.",
    "O EPI no corpo é segurança na alma.",
    "Não espere o acidente acontecer, faça a prevenção agora.",
    "Acidentes não ocorrem por acaso, mas por descaso.",
    "A atenção aos detalhes salva vidas.",
    "Reportar incidentes é prevenir acidentes."
]

# Função para gerar frases do mês
def gerar_frases_mes(ano, mes):
    dias_no_mes = monthrange(ano, mes)[1]
    frases_do_mes = []
    frases_disponiveis = frases_dds.copy()
    
    for dia in range(1, dias_no_mes + 1):
        if not frases_disponiveis:
            frases_disponiveis = frases_dds.copy()
        frase_sorteada = random.choice(frases_disponiveis)
        frases_disponiveis.remove(frase_sorteada)
        frases_do_mes.append({
            "Data": f"{ano}-{mes:02d}-{dia:02d}",
            "Frase DDS": frase_sorteada
        })

    return frases_do_mes

# Função principal
def main():
    ano = int(input("Digite o ano (ex: 2025): "))
    mes = int(input("Digite o mês (1-12): "))
    frases_para_mes = gerar_frases_mes(ano, mes)
    
    print("\nFrases sorteadas para o mês:")
    for item in frases_para_mes:
        print(f"{item['Data']}: {item['Frase DDS']}")

if __name__ == "__main__":
    main()
# Sorteador de Frases DDS

Este projeto permite gerar **uma frase diária de DDS** (Diálogo Diário de Segurança)

## Como usar

1. Clone o repositório:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o script:
```bash
python dds_sorteador.py
```

4. Digite o ano e o mês desejado e será gerada com uma frase para cada dia do mês.

## Estrutura do projeto
- `dds_sorteador.py` → Script principal que gera as frases e salva.
- `requirements.txt` → Dependências do projeto.
- `README.md` → Este arquivo explicativo.

## Observações
- As frases são sorteadas aleatoriamente e garantem que todas sejam usadas antes de repetir.
- Você pode adicionar ou modificar frases editando a lista `frases_dds` no script.

import pandas as pd
from faker import Faker

# Caminho para seu arquivo original
caminho_arquivo = "" # Colocar o arquivo

# Inicializa o gerador de nomes falsos
faker = Faker('pt_BR')

# Carrega a planilha correta (ajuste se necessário)
df = pd.read_excel(caminho_arquivo, sheet_name='2-FUNCIONARIOS', header=1)

# Gera nomes fictícios únicos para cada matrícula
matriculas_unicas = df['MATRICULA'].dropna().unique()
nomes_ficticios = {mat: faker.name() for mat in matriculas_unicas}

# Substitui a coluna NOME com base na matrícula
df['NOME'] = df['MATRICULA'].map(nomes_ficticios)

# Salva o novo arquivo
df.to_excel("Pendencia_atual_anonimizado.xlsx", index=False)

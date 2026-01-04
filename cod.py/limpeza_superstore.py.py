import pandas as pd
from sqlalchemy import create_engine

#   conectando banco de dados
host = 'localhost'
user = 'root'
password = '0933'
database = 'bd_analise_de_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#   importando dados
df = pd.read_sql('SELECT * FROM superstore', engine)
# print('\n', df.head(10))

#   limpeza de dados (datas, nulos, tipos)

#   datas
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

#   tipos 
for col in ['sales', 'quantity', 'discount', 'profit']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

#   colunas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#   nulos
df = df.fillna({
    'postal_code': 0,
    'region': 'Desconhecido',
    'category': 'Desconhecido',
})

#   exportando dados
df.to_sql('superstore', engine, if_exists='replace', index=False)
print('\n', df.head(10))
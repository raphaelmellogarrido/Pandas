import pandas as pd

data = pd.read_csv('telecom.csv', index_col = 0) #Dessa maneira exclui o "unnamed 0"

df = pd.DataFrame(data) #criar uma dataframe com o arquivo data(telecome.csv)
df['ServicoTelefone'] #mostrar apenas a coluna 'ServicoTelefone'
df.drop(columns=['MultiplasLinhas']) #deletar a coluna MultiplasLinhas
df[['Genero', 'Casado', 'ServicoTelefone']] #Mostrar as colunas 'Genero, Casado, ServicoTelefone'
df.rename(columns = {'ServicoTelefone':'Telefone'})
#para computar as alterações precisamos validar. No caso df.rename(columns = {'ServicoTelefone':'Telefone'})
df.sort_values('MesesComoCliente') #Faz com que coloque em forma crescente a coluna selecionada
df.head(5) #mostrar os 5 primeiros resultados
df.tail(5) #mostrar os 5 ultimos resultados
df.set_index('Casado') #transformar 'casado' como primeira coluna (index)
len(df.index) #mostrar quantas linhas
df[df['Casado'].map(lambda title: 'Nao' in title)] #mostra apenas os clientes não casados da coluna 'Casado'
df.loc[df['IDCliente'] == '4795-UXVCJ'] #mostra a linha inteira que contem o id pedido '4795-UXVCJ'
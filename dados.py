#Importação de módulos e arquivos
import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',') #Define o separador como ';', e o decimal=','.)
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

#Retirar colunas de Estado Civil e Cargo da tabela de funcionários
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
print(funcionarios_df)
print(clientes_df)
print(servicos_df)


#Valor total da folha salarial
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total da Folha Salarial Mensal é de: R${:,}'.format(funcionarios_df['Salario Total'].sum()))

#Faturamento da empresa
faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']
print('Total do Faturamento da Empresa é de: R${:,}'.format(faturamentos_df['Faturamento Total'].sum()))

#Percentual de funcionários que fecharam contratos
qtde_funcionario_fecharam_contrato = len(servicos_df['ID Funcionário'].unique())
qtde_funcionario_total = len(funcionarios_df['ID Funcionário'])
print('O Percentual de Funcionários que Fecharam Contratos é de:{:.2%}'.format(qtde_funcionario_fecharam_contrato / qtde_funcionario_total))

#Quantidade de contratos por área
contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário',"Area"]], on='ID Funcionário')
contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)


#Quantidade de funcionários por área
funcionarios_por_area_qtde = funcionarios_df['Area'].value_counts()
print(funcionarios_por_area_qtde)

#Ticket médio mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('Ticket Médio Mensal R$:{:,.2f}'.format(ticket_medio))
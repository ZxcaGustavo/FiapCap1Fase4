import cx_Oracle
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import warnings

# Configuração para evitar warnings desnecessários
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


# Treinamento do modelo preditivo
def treinar_modelo():
    # Dados fictícios para treinamento
    data = {
        'temperatura': [20, 22, 25, 28, 30, 32, 24],
        'umidade': [70, 65, 60, 50, 40, 30, 55],
        'ldr': [400, 300, 200, 100, 500, 600, 450],
        'botao1': [0, 1, 0, 1, 0, 1, 0],
        'botao2': [0, 0, 1, 1, 0, 1, 1],
        'irrigar': [1, 1, 1, 0, 0, 0, 1]  # 1 = Sim, 0 = Não
    }
    df = pd.DataFrame(data)

    # Separar features (X) e target (y)
    X = df[['temperatura', 'umidade', 'ldr', 'botao1', 'botao2']]
    y = df['irrigar']

    # Treinar o modelo
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X, y)
    return modelo


modelo = treinar_modelo()


# Função para conectar ao banco de dados Oracle
def conectar_oracle():
    try:
        usuario = 'sys'
        senha = 'carro'
        dsn = cx_Oracle.makedsn("desktop-qv69de7", 1521, service_name="XE")
        conexao = cx_Oracle.connect(user=usuario, password=senha, dsn=dsn, mode=cx_Oracle.SYSDBA)
        return conexao
    except cx_Oracle.DatabaseError as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Funções para obter dados do banco
def consultar_historico(conexao):
    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM dados_sensores ORDER BY data_hora DESC"
        cursor.execute(query)
        resultado = cursor.fetchall()
        colunas = [col[0] for col in cursor.description]
        df = pd.DataFrame(resultado, columns=colunas)
        return df
    except cx_Oracle.Error as e:
        st.error(f"Erro ao consultar histórico: {e}")
        return pd.DataFrame()


def prever_irrigacao_por_id(conexao, modelo, id_registro):
    try:
        cursor = conexao.cursor()
        query = "SELECT temperatura, umidade, ldr, botao1, botao2 FROM dados_sensores WHERE id = :id"
        cursor.execute(query, [id_registro])
        resultado = cursor.fetchone()

        if resultado:
            # Criar um DataFrame com os dados para a predição
            colunas = ['temperatura', 'umidade', 'ldr', 'botao1', 'botao2']
            df_dados = pd.DataFrame([resultado], columns=colunas)
            previsao = modelo.predict(df_dados)
            return "Sim" if previsao[0] == 1 else "Não"
        else:
            st.warning("ID não encontrada no banco de dados.")
            return None
    except cx_Oracle.Error as e:
        st.error(f"Erro ao prever irrigação: {e}")
        return None


# Streamlit App
st.title("Dashboard de Irrigação - FarmTech Solutions")

# Conexão com o banco de dados
conexao = conectar_oracle()

if conexao:
    # Seção de Histórico de Dados
    st.subheader("Histórico de Dados")
    historico_df = consultar_historico(conexao)
    if not historico_df.empty:
        st.dataframe(historico_df)
    else:
        st.write("Nenhum dado disponível.")

    # Previsão de Irrigação
    st.subheader("Previsão de Irrigação")
    id_input = st.number_input("Digite o ID para prever a irrigação:", min_value=1, step=1)

    if st.button("Prever"):
        previsao = prever_irrigacao_por_id(conexao, modelo, id_input)
        if previsao:
            st.success(f"Previsão de irrigação para ID {id_input}: {previsao}")

    # Fechar conexão
    conexao.close()
else:
    st.error("Não foi possível conectar ao banco de dados.")
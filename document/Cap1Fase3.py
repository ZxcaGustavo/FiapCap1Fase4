import cx_Oracle
from datetime import datetime



# Configuração da conexão com o banco de dados Oracle
def conectar_oracle():
    try:
        usuario = 'sys'
        senha = 'carro'
        dsn = cx_Oracle.makedsn("desktop-qv69de7", 1521, service_name="XE")
        conexao = cx_Oracle.connect(user=usuario, password=senha, dsn=dsn, mode=cx_Oracle.SYSDBA)
        return conexao
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Funções CRUD
def inserir_dados(conexao):
    try:
        temperatura = float(input("Digite a temperatura: "))
        umidade = float(input("Digite a umidade: "))
        ldr = int(input("Digite o valor do LDR: "))
        botao1 = int(input("Digite o estado do botão 1 (0 ou 1): "))
        botao2 = int(input("Digite o estado do botão 2 (0 ou 1): "))
        rele = int(input("Digite o estado do relé (0 ou 1): "))

        cursor = conexao.cursor()
        query = """INSERT INTO dados_sensores 
                   (temperatura, umidade, ldr, botao1, botao2, rele)
                   VALUES (:1, :2, :3, :4, :5, :6)"""
        dados = (temperatura, umidade, ldr, botao1, botao2, rele)
        cursor.execute(query, dados)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    except cx_Oracle.Error as e:
        print("Erro ao inserir dados:", e)

def consultar_historico(conexao):
    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM dados_sensores ORDER BY data_hora DESC"
        cursor.execute(query)
        resultado = cursor.fetchall()
        for linha in resultado:
            print("ID:", linha[0], "Data/Hora:", linha[1], "Temperatura:", linha[2],
                  "Umidade:", linha[3], "LDR:", linha[4], "Botão 1:", linha[5],
                  "Botão 2:", linha[6], "Relé:", linha[7])
    except cx_Oracle.Error as e:
        print("Erro ao consultar histórico:", e)

def atualizar_dados(conexao):
    try:
        id_registro = int(input("Digite o ID do registro a ser atualizado: "))
        temperatura = input("Digite a nova temperatura (ou deixe em branco para não alterar): ")
        umidade = input("Digite a nova umidade (ou deixe em branco para não alterar): ")
        ldr = input("Digite o novo valor do LDR (ou deixe em branco para não alterar): ")
        botao1 = input("Digite o novo estado do botão 1 (ou deixe em branco para não alterar): ")
        botao2 = input("Digite o novo estado do botão 2 (ou deixe em branco para não alterar): ")
        rele = input("Digite o novo estado do relé (ou deixe em branco para não alterar): ")

        cursor = conexao.cursor()
        campos = []
        valores = []

        # Verificar cada campo e adicionar apenas os não vazios
        if temperatura:
            campos.append("temperatura = :temp")
            valores.append(float(temperatura))
        if umidade:
            campos.append("umidade = :umid")
            valores.append(float(umidade))
        if ldr:
            campos.append("ldr = :ldr")
            valores.append(int(ldr))
        if botao1:
            campos.append("botao1 = :botao1")
            valores.append(int(botao1))
        if botao2:
            campos.append("botao2 = :botao2")
            valores.append(int(botao2))
        if rele:
            campos.append("rele = :rele")
            valores.append(int(rele))

        valores.append(id_registro)
        query = f"UPDATE dados_sensores SET {', '.join(campos)} WHERE id = :id"
        cursor.execute(query, valores)
        conexao.commit()
        print("Dados atualizados com sucesso.")
    except cx_Oracle.Error as e:
        print("Erro ao atualizar dados:", e)

def deletar_dados(conexao):
    try:
        id_registro = int(input("Digite o ID do registro a ser deletado: "))
        cursor = conexao.cursor()
        query = "DELETE FROM dados_sensores WHERE id = :id"
        cursor.execute(query, [id_registro])
        conexao.commit()
        print("Dados deletados com sucesso.")
    except cx_Oracle.Error as e:
        print("Erro ao deletar dados:", e)

# Função principal para exibir o menu
def menu():
    conexao = conectar_oracle()
    if not conexao:
        print("Falha ao conectar com o banco de dados. Encerrando o programa.")
        return

    while True:
        print("\nEscolha uma operação:")
        print("1. Inserir dados")
        print("2. Consultar histórico")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            inserir_dados(conexao)
        elif opcao == '2':
            consultar_historico(conexao)
        elif opcao == '3':
            atualizar_dados(conexao)
        elif opcao == '4':
            deletar_dados(conexao)
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conexao.close()

# Executa o menu principal
menu()




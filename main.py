from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import csv

app = Flask(__name__)

# Configurações do banco de dados

app.config["MYSQL_USER"] = "Digite seu usuário"
app.config["MYSQL_PASSWORD"] = "Digite sua senha"
app.config["MYSQL_DB"] = "Digite o nome de seu banco"
app.config["MYSQL_DATABASE_HOST"] = "Digite seu host MySQL"


# Inicializa a extensão MySQL com o app Flask
mysql = MySQL(app)


# Cria a tabela "contato" e importe os dados do arquivo CSV
@app.route("/tabela_contatos", methods=["POST"])
def tabela_contatos():
    try:
        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Cria a tabela "contato" se já não existir.
        criar_tabela_query = """
        CREATE TABLE IF NOT EXISTS contato (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(100),
            Sobrenome VARCHAR(100),
            Email VARCHAR(100),
            Telefone VARCHAR(20)
        )
        """
        cursor.execute(criar_tabela_query)

        # Abre o arquivo CSV e importa os dados para a tabela "contato"
        with open("TesteAxya.csv", "r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Pula a primeira linha (cabeçalho do CSV)

            # Insere cada registro do CSV na tabela "contato"
            for row in csv_reader:
                sql = "INSERT INTO contato (ID, Nome, Sobrenome, Email, Telefone) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, tuple(row))

            # Confirma a inserção dos dados no banco
            mysql.connection.commit()

        return 'Tabela "contato" criada e dados do CSV importados com sucesso!'

    except Exception as e:
        return f"Ocorreu um erro: {e}"
    finally:
        # Fecha o cursor, se ele foi criado
        if cursor:
            cursor.close()


# CRUDS


# CREATE
@app.route("/contato", methods=["POST"])
def criar_contato():
    try:
        # Obtém os dados do JSON enviados pela requisição
        data = request.get_json()
        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Cria um novo contato
        criar_contato_query = f"""INSERT INTO contato (
Nome,Sobrenome,Email,Telefone) VALUES ("{data['Nome']}", "{data['Sobrenome']}", "{data['Email']}","{data['Telefone']}")"""
        cursor.execute(criar_contato_query)

        # Obtém o ID do último registro inserido
        novo_id = cursor.lastrowid

        # Confirma a inserção dos dados no banco
        mysql.connection.commit()

        return jsonify({"mensagem": f"Contato criado com sucesso com o id {novo_id}!"})

    except Exception as e:
        return jsonify({"Ocorreu um erro: ": str(e)}), 500

    finally:
        # Feche o cursor, se ele foi criado
        if cursor:
            cursor.close()


# READ
@app.route("/contato/<contato_id>", methods=["GET"])
def ler_contato(contato_id):
    try:
        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Consulta para obter as informações do contato com base no ID
        ler_contato_query = f"SELECT * FROM contato WHERE ID = {contato_id}"
        cursor.execute(ler_contato_query)

        # Obtenha o resultado da consulta
        contato = cursor.fetchone()

        if not contato:
            return jsonify({"mensagem": "Contato não encontrado."}), 404

        # Converta o resultado em um json para facilitar o entendimento após a chamada da rota
        contato_dict = {
            "ID": contato[0],
            "Nome": contato[1],
            "Sobrenome": contato[2],
            "Email": contato[3],
            "Telefone": contato[4],
        }
        return jsonify(contato_dict)
    except Exception as e:
        return jsonify({"Ocorreu um erro: ": str(e)}), 500
    finally:
        # Feche o cursor, se ele foi criado
        if cursor:
            cursor.close()


# UPDATE
@app.route("/contato/<contato_id>", methods=["PUT"])
def atualizar_contato(contato_id):
    try:
        # Obtenha os dados do JSON enviado pelo Postman
        data = request.get_json()

        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Consulta para obter as informações do contato com base no ID
        atualizar_contato_query = f"UPDATE contato SET Nome = '{data['Nome']}', Sobrenome = '{data['Sobrenome']}', Email = '{data['Email']}', Telefone = '{data['Telefone']}' WHERE ID = {contato_id}"
        cursor.execute(atualizar_contato_query)

        # Confirma a atualização dos dados no banco
        mysql.connection.commit()

        return jsonify({"mensagem": "Contato atualizado com sucesso!"})
    except Exception as e:
        return jsonify({"Ocorreu um erro: ": str(e)}), 500
    finally:
        # Feche o cursor, se ele foi criado
        if cursor:
            cursor.close()


# DELETE
@app.route("/contato/<contato_id>", methods=["DELETE"])
def deletar_contato(contato_id):
    try:
        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Consulta para obter as informações do contato com base no ID
        deletar_contato_query = f"DELETE FROM contato WHERE ID={contato_id}"
        cursor.execute(deletar_contato_query)

        # Confirma a atualização dos dados no banco
        mysql.connection.commit()

        return jsonify({"mensagem": "Contato deletado com sucesso!"})
    except Exception as e:
        return jsonify({"Ocorreu um erro: ": str(e)}), 500
    finally:
        # Feche o cursor, se ele foi criado
        if cursor:
            cursor.close()


# SEARCH
@app.route("/contato", methods=["GET"])
def buscar_contato():
    try:
        # Obtenha o parâmetro de pesquisa do nome da query string
        query_string = request.args.get("nome")

        # Se conecta ao banco de dados MySQL e cria o cursor
        cursor = mysql.connection.cursor()

        # Consulta para obter as informações do contato com base no ID
        buscar_query = f"SELECT * FROM contato WHERE Nome LIKE '%{query_string}%'"
        cursor.execute(buscar_query)

        # Obtenha os resultados da consulta
        contatos = cursor.fetchall()

        # Crie uma lista de dicionários contendo os contatos encontrados
        contatos_encontrados = []
        for contato in contatos:
            contato_dict = {
                "ID": contato[0],
                "Nome": contato[1],
                "Sobrenome": contato[2],
                "Email": contato[3],
                "Telefone": contato[4],
            }
            contatos_encontrados.append(contato_dict)

        return jsonify(contatos_encontrados)

    except Exception as e:
        return jsonify({"Ocorreu um erro: ": str(e)}), 500
    finally:
        # Feche o cursor, se ele foi criado
        if cursor:
            cursor.close()


if __name__ == "__main__":
    app.run()

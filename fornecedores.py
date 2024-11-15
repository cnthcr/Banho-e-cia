from db_connection import connect_to_database

def cadastrar_fornecedor(fornecedor, telefone):
    """Cadastra um novo fornecedor no banco de dados."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO fornecedores (fornecedor, telefone) VALUES (%s, %s)"
        values = (fornecedor, telefone)
        cursor.execute(query, values)
        connection.commit()
        print("Fornecedor cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar fornecedor: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

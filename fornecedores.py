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

def mostrar_fornecedor(id_fornecedor):
    """Exibe as informações de um fornecedor específico pelo ID."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM fornecedores WHERE id = %s"
        cursor.execute(query, (id_fornecedor,))
        fornecedor = cursor.fetchone()
        if fornecedor:
            print("Fornecedor encontrado:")
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Telefone: {fornecedor[2]}")
        else:
            print("Fornecedor não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar fornecedor: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
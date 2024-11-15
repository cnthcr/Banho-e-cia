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


def atualizar_fornecedor(id_fornecedor, nome=None, telefone=None):
    """Atualiza as informações de um fornecedor existente."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()

        updates = []
        values = []

        if nome:
            updates.append("nome = %s")
            values.append(nome)
        if telefone:
            updates.append("telefone = %s")
            values.append(telefone)

        if not updates:
            print("Nenhum campo para atualizar.")
            return

        query = f"UPDATE fornecedores SET {', '.join(updates)} WHERE id = %s"
        values.append(id_fornecedor)

        cursor.execute(query, tuple(values))
        connection.commit()
        print("Fornecedor atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar fornecedor: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def deletar_fornecedor(id_fornecedor):
    """Deleta um fornecedor do banco de dados pelo ID."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM fornecedores WHERE id = %s"
        cursor.execute(query, (id_fornecedor,))
        connection.commit()
        print("Fornecedor deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar fornecedor: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()


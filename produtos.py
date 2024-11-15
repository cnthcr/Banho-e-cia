from db_connection import connect_to_database

def cadastrar_produto(nome, marca, tamanho, cor, quantidade, preco, fornecedor_id):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO produtos (nome, marca, tamanho, cor, quantidade, preco, fornecedor_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (nome, marca, tamanho, cor, quantidade, preco, fornecedor_id)
        cursor.execute(query, values)
        connection.commit()
        print("Produto cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

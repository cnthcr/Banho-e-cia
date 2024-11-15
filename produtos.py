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
            
def mostrar_produto(id_produto):
    """Exibe as informações de um produto específico pelo ID."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM produtos WHERE id = %s"
        cursor.execute(query, (id_produto,))
        produto = cursor.fetchone()
        if produto:
            print("Produto encontrado:")
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Marca: {produto[2]}, Tamanho: {produto[3]}")
            print(f"Cor: {produto[4]}, Quantidade: {produto[5]}, Preço: {produto[6]}, Fornecedor ID: {produto[7]}")
        else:
            print("Produto não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

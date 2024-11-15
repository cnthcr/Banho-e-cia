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


def atualizar_produto(id_produto, nome=None, marca=None, tamanho=None, cor=None, quantidade=None, preco=None,
                      fornecedor_id=None):
    """Atualiza as informações de um produto existente."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()

        # Constrói dinamicamente a query com os valores fornecidos
        updates = []
        values = []

        if nome:
            updates.append("nome = %s")
            values.append(nome)
        if marca:
            updates.append("marca = %s")
            values.append(marca)
        if tamanho:
            updates.append("tamanho = %s")
            values.append(tamanho)
        if cor:
            updates.append("cor = %s")
            values.append(cor)
        if quantidade is not None:
            updates.append("quantidade = %s")
            values.append(quantidade)
        if preco is not None:
            updates.append("preco = %s")
            values.append(preco)
        if fornecedor_id:
            updates.append("fornecedor_id = %s")
            values.append(fornecedor_id)

        # Se não houver nenhuma atualização a ser feita
        if not updates:
            print("Nenhum campo para atualizar.")
            return

        # Constrói a query final
        query = f"UPDATE produtos SET {', '.join(updates)} WHERE id = %s"
        values.append(id_produto)

        cursor.execute(query, tuple(values))
        connection.commit()
        print("Produto atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def deletar_produto(id_produto):
    """Deleta um produto do banco de dados pelo ID."""
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(query, (id_produto,))
        connection.commit()
        print("Produto deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

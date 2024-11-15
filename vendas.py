from db_connection import connect_to_database
from datetime import date

def realizar_venda(id_produto, quantidade):
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        
        cursor.execute("SELECT quantidade FROM produtos WHERE id = %s", (id_produto,))
        result = cursor.fetchone()
        if result and int(result[0]) >= quantidade:

            cursor.execute("UPDATE produtos SET quantidade = quantidade - %s WHERE id = %s", (quantidade, id_produto))
            
            
            query = "INSERT INTO vendas (id_produto, data_venda, id_cliente, quantidade) VALUES (%s, %s, %s, %s)"
            values = (id_produto, date.today(), None, quantidade)
            cursor.execute(query, values)
            connection.commit()
            print("Venda realizada com sucesso.")
        else:
            print("Estoque insuficiente para realizar a venda.")
    except Exception as e:
        print(f"Erro ao realizar venda: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def visualizar_top_vendas():
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        query = """
            SELECT p.nome, SUM(v.quantidade) AS total_vendido
            FROM vendas v
            JOIN produtos p ON v.id_produto = p.id
            GROUP BY v.id_produto
            ORDER BY total_vendido DESC
            LIMIT 5
        """
        cursor.execute(query)
        top_vendas = cursor.fetchall()
        print("Top 5 Vendas:")
        for venda in top_vendas:
            print(f"Produto: {venda[0]}, Quantidade Vendida: {venda[1]}")
    except Exception as e:
        print(f"Erro ao visualizar top vendas: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()



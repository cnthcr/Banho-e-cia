from produtos import *

def main():
    while True:
        print("\nMenu Principal")
        print("1. Vendas")
        print("2. Produtos")
        print("3. Fornecedores")
        print("4. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            pass
        elif choice == '2':
            while True:
                print("\nMenu Produtos")
                print("1. Cadastrar Produto")
                print("2. Mostrar Produto Específico")
                print("3. Atualizar Produto")
                print("4. Deletar Produto")
                print("5. Listar Todos os Produtos")
                print("6. Voltar")

                sub_choice = input("Escolha uma opção: ")
                if sub_choice == '1':
                    nome = input("Nome do produto: ")
                    marca = input("Marca do produto: ")
                    tamanho = input("Tamanho do produto: ")
                    cor = input("Cor do produto: ")
                    quantidade = int(input("Quantidade em estoque: "))
                    preco = float(input("Preço do produto: "))
                    fornecedor_id = int(input("ID do fornecedor: "))
                    cadastrar_produto(nome, marca, tamanho, cor, quantidade, preco, fornecedor_id)
                elif sub_choice == '2':
                    id_produto = int(input("ID do produto: "))
                    mostrar_produto(id_produto)
                elif sub_choice == '3':
                    id_produto = int(input("ID do produto a atualizar: "))
                    nome = input("Novo nome (deixe em branco para não alterar): ")
                    marca = input("Nova marca (deixe em branco para não alterar): ")
                    tamanho = input("Novo tamanho (deixe em branco para não alterar): ")
                    cor = input("Nova cor (deixe em branco para não alterar): ")
                    quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
                    preco = input("Novo preço (deixe em branco para não alterar): ")
                    fornecedor_id = input("Novo ID do fornecedor (deixe em branco para não alterar): ")

                    quantidade = int(quantidade) if quantidade else None
                    preco = float(preco) if preco else None
                    fornecedor_id = int(fornecedor_id) if fornecedor_id else None

                    atualizar_produto(id_produto, nome or None, marca or None, tamanho or None,
                                      cor or None, quantidade, preco, fornecedor_id)
                elif sub_choice == '4':
                    id_do_produto = int(input('Digite o id do produro: '))
                    deletar_produto(id_do_produto)
                elif sub_choice == '5':
                    listar_produtos()
                elif sub_choice == '6':
                    pass
        elif choice == '3':
            pass
        elif choice == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

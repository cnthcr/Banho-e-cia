from produtos import *
from fornecedores import *

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
                    id_do_produto = int(input("Digite o id do produro: "))
                    deletar_produto(id_do_produto)
                elif sub_choice == '5':
                    listar_produtos()
                elif sub_choice == '6':
                    break
                else:
                    print("Opção inválida")
        elif choice == '3':
            while True:
                print("\nMenu Fornecedores")
                print("1. Cadastrar Fornecedor")
                print("2. Mostrar Fornecedor Específico")
                print("3. Atualizar Fornecedor")
                print("4. Deletar Fornecedor")
                print("5. Listar Todos os Fornecedores")
                print("6. Voltar")

                sub_choice = input("Escolha uma opção: ")
                if sub_choice == '1':
                    nome = input("Nome do fornecedor: ")
                    telefone = input("Telefone do fornecedor: ")
                    cadastrar_fornecedor(nome, telefone)
                elif sub_choice == '2':
                    id_fornecedor = int(input("ID do fornecedor: "))
                    mostrar_fornecedor(id_fornecedor)
                elif sub_choice == '3':
                    id_fornecedor = int(input("ID do fornecedor a atualizar: "))
                    nome = input("Novo nome (deixe em branco para não alterar): ")
                    telefone = input("Novo telefone (deixe em branco para não alterar): ")

                    atualizar_fornecedor(id_fornecedor, nome or None, telefone or None)
                elif sub_choice == '4':
                    id_fornecedor = int(input("ID do fornecedor a deletar: "))
                    deletar_fornecedor(id_fornecedor)
                elif sub_choice == '5':
                    pass
                elif sub_choice == '6':
                    break
                else:
                    print("Opção inválida.")
        elif choice == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

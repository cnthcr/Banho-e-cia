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
                    pass
                elif sub_choice == '4':
                    pass
                elif sub_choice == '5':
                    pass
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

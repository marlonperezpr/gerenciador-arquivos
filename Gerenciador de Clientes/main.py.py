import json


class GerenciadorClientes:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, id_cliente, nome, email):
        if id_cliente in self.clientes:
            print(f"Cliente com ID {id_cliente} já existe")
        else:
            self.clientes[id_cliente] = {
                'nome': nome,
                'email': email,
                'produtos': []
            }
            print(f"Cliente {nome} adicionado com sucesso")

    def adicionar_produto(self, id_cliente, nome_produto, cor, preco):
        if id_cliente in self.clientes:
            self.clientes[id_cliente]['produtos'].append({
                'nome': nome_produto,
                'cor': cor,
                'preco': preco
            })
            print(f"Produto {nome_produto} adicionado ao cliente {self.clientes[id_cliente]['nome']}")

        else:
            print(f"Cliente com ID {id_cliente} não existe")

    def listar_clientes(self):
        for id_cliente, info in self.clientes.items():
            print(f"ID: {id_cliente}")
            print(f"Nome: {info['nome']}")
            print(f"Email: {info['email']}")
            print("Produtos: ")
            for produto in info['produtos']:
                print(f" Nome: {produto['nome']}, Cor: {produto['cor']}, preço: {produto['preco']}")
            print("")

    def deletar_produto(self, id_cliente, nome_produto):
        if id_cliente in self.clientes:
            produtos = self.clientes[id_cliente]['produtos']
            for produto in produtos:
                if produto['nome'] == nome_produto:
                    produtos.remove(produto)
                    print(f"Produto {nome_produto} removido do cliente {self.clientes[id_cliente]['nome']}.")
                    return
            print(f"Produto {nome_produto} não encontrado para o cliente{self.clientes[id_cliente]['nome']}")
        else:
            print(f"Cliente com ID {id_cliente} não existe.")

    def editar_cliente(self, id_cliente, nome=None, email=None):
        if id_cliente in self.clientes:
            if nome:
                self.clientes[id_cliente]['nome'] = nome
                print(f"Nome do cliente {id_cliente} atualizado para {nome}.")
            if email:
                self.clientes[id_cliente]['email'] = email
                print(f"Email do cliente {id_cliente} atualizado para {email}.")
        else:
            print(f"Cliente com ID {id_cliente} não existe.")
    
    def salvar_dados(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(self.clientes, f)
        print(f"Dados salvos em {arquivo}.")
    
    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.clientes = json.load(f)
            print(f"Arquivo {arquivo} não encontrado")
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado.")    

    def gerar_relatorio(self, id_cliente=None):
        if id_cliente:
            if id_cliente in self.clientes:
                cliente = self.clientes[id_cliente]
                print(f"Relatório do Cliente {cliente['nome']}")
                print(f"ID: {id_cliente}")
                print(f"Nome: {cliente['nome']}")
                print(f"Email: {cliente['email']}")
                print("Produtos: ")
                for produto in cliente['produtos']:
                    print(f" nome: {produto['nome']}, cor: {produto['cor']}, preço: {produto['preco']}")

            else:
                print(f"Cliente com ID {id_cliente} não existe.")
        else:
            print("Relatório de todos os Clientes:")
            for id_cliente, info in self.clientes.items():
                print(f"ID: {id_cliente}")
                print(f"Nome: {info['nome']}")
                print(f"Email: {info['email']}")
                print("Produtos:")
                for produto in info['produtos']:
                    print(f"  nome: {produto['nome']}, cor: {produto['cor']}, preco: {produto['preco']}")
                print("")
def main():
    gerenciador = GerenciadorClientes()
    while True:
        print("\nMenu:")
        print("1. Adicionar Cliente")
        print("2. Adicionar Produto")
        print("3. Listar Clientes")
        print("4. Deletar Produto")
        print("5. Editar Cliente")
        print("6. Salvar Dados")
        print("7. Carregar Dados")
        print("8. Gerar Relatório")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id_cliente = input("ID do cliente: ")
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            gerenciador.adicionar_cliente(id_cliente, nome, email)

        elif escolha == '2':
            id_cliente = input("ID do Cliente: ")
            nome_produto = input("Nome do Produto: ")
            cor = input("Cor do Produto: ")
            preco = float(input("Preço do produto: "))
            gerenciador.adicionar_produto(id_cliente, nome_produto, cor, preco)
        
        elif escolha == '3':
            gerenciador.listar_clientes()

        elif escolha == '4':
            id_cliente = input("ID do Cliente: ")
            nome_produto = input("Nome do produto a ser deletado: ")
            gerenciador.deletar_produto(id_cliente, nome_produto)

        elif escolha == '5':
            id_cliente = input("ID do cliente: ")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            email = input("Novo Email (deixe em branco para não alterar): ")
            gerenciador.editar_cliente(id_cliente, nome, email)
        
        elif escolha == '6':
            arquivo = input("Nome do arquivo: ")
            gerenciador.salvar_dados(arquivo)

        elif escolha == '7':
            arquivo = input("Nome do arquivo: ")
            gerenciador.carregar_dados(arquivo)
        
        elif escolha == '8':
            id_cliente = input("ID do Cliente (deixe em branco para relatório de todos os clientes): ")
            gerenciador.gerar_relatorio(id_cliente)
        
        elif escolha == '9':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()



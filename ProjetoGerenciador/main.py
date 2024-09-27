class Tarefa:
    def __init__(self, nome, descricao, prioridade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.concluida = False

    def __str__(self):
        status = "Concluída" if self.concluida else "Não concluída"
        return f"{self.nome}: {self.descricao} ({self.prioridade} - {self.categoria} - {status})"

tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def listar_tarefas():
    for tarefa in tarefas:
        print(tarefa)

def marcar_concluida(nome_tarefa):
    for tarefa in tarefas:
        if tarefa.nome == nome_tarefa:
            tarefa.concluida = True
            print(f"\033[92mTarefa '{nome_tarefa}' marcada como concluída\033[0m")
            return
    print(f"\033[91mTarefa '{nome_tarefa}' não encontrada\033[0m")

def exibir_por_prioridade(prioridade):
    for tarefa in tarefas:
        if tarefa.prioridade == prioridade:
            print(tarefa)

def exibir_por_categoria(categoria):
    for tarefa in tarefas:
        if tarefa.categoria == categoria:
            print(tarefa)

def menu():
    while True:
        print("\033[94m== Menu de Comandos ==\033[0m")
        print(" 1. Adicionar tarefa")
        print(" 2. Listar Tarefas")
        print(" 3. Marcar tarefa como concluída")
        print(" 4. Exibir tarefas por prioridade")
        print(" 5. Exibir por categoria")
        print(" 6. Sair")
        opcao = input("Escolha sua opção: ")
        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa: ")
            categoria = input("Categoria da tarefa: ")
            tarefa = Tarefa(nome, descricao, prioridade, categoria)
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            nome_tarefa = input("Coloque o nome da tarefa que vais concluir: ")
            marcar_concluida(nome_tarefa)
        elif opcao == "4":
            prioridade = input("Prioridade da tarefa: ")
            exibir_por_prioridade(prioridade)
        elif opcao == "5":
            categoria = input("Categoria da tarefa: ")
            exibir_por_categoria(categoria)
        elif opcao == "6":
            print("\033[1;31mDesligando...\033[0m")
            break
        else:
            print("\033[91mOpção inválida. Tente novamente.\033[0m")

menu()

#Recomendado: (Ativar o venv e digitar "python main.py ou py main.py")
#tentei upar a pasta no github com venv não deu certo...
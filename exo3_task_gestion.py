# Mireole#8364
# Exercice 3 : Gérez vos tâches

class PermissionError(Exception):
    pass


class Account:
    def __init__(self, name, can_manage_tasks, can_manage_users):
        self.name = name
        self.can_manage_tasks = can_manage_tasks
        self.can_manage_users = can_manage_users


class AccountManager:
    def __init__(self):
        self.accounts = []
        self.accounts.append(Account("Administrateur", True, True))
        self.active_account = self.get_account("Administrateur")

    def add_account(self, account):
        if not self.active_account.can_manage_users:
            raise PermissionError("Vous n'avez pas la permission de gérer les comptes.")
        if [True for registered_account in self.accounts if registered_account.name == account.name]:
            raise ValueError("Le compte avec le nom {} existe déjà.".format(account.name))
        self.accounts.append(account)

    def delete_account(self, account):
        if not self.active_account.can_manage_users:
            raise PermissionError("Vous n'avez pas la permission de gérer les comptes.")
        self.accounts.remove(account)

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        raise ValueError("Le compte avec le nom {} n'existe pas.".format(name))

    def connect(self, name):
        self.active_account = self.get_account(name)


class Task:
    def __init__(self, name, description, accounts):
        self.name = name
        self.description = description
        self.accounts = accounts
        self.done = False

    def set_done(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self, account):
        if account.can_manage_tasks:
            return self.tasks
        return [task for task in self.tasks if account in task.accounts]

    def delete_task(self, task_name, account):
        if account.can_manage_tasks:
            self.tasks = [task for task in self.tasks if task.name != task_name]
        else:
            raise PermissionError("Vous n'avez pas la permission de gérer les tâches.")

    def clear_tasks(self, account):
        if account.can_manage_tasks:
            self.tasks = []
        else:
            raise PermissionError("Vous n'avez pas la permission de gérer les tâches.")


class Command:
    def __init__(self, name, account_manager, task_manager):
        self.name = name
        self.account_manager = account_manager
        self.task_manager = task_manager

    def execute(self):
        pass


class AddTaskCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("ajouter", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        description = input("Description de la tâche : ")
        accounts = input("Comptes associés (séparés par des virgules) : ").split(",")
        for i in range(len(accounts)):
            accounts[i] = self.account_manager.get_account(accounts[i])
        self.task_manager.add_task(Task(name, description, accounts))


class DeleteTaskCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("retirer", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        self.task_manager.delete_task(name, self.account_manager.active_account)


class MarkTaskAsDoneCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("compléter", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        for task in self.task_manager.get_tasks(self.account_manager.active_account):
            if task.name == name:
                task.set_done()
                return
        raise ValueError("La tâche {} n'existe pas ou vous n'y avez pas accès.".format(name))


class ListTasksCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("liste", account_manager, task_manager)

    def execute(self):
        if self.task_manager.get_tasks(self.account_manager.active_account) == []:
            print("Vous n'avez aucune tâche. Profitez du répit !")
            return
        max_name_length = max(len("Nom"), max(
            [len(task.name) for task in self.task_manager.get_tasks(self.account_manager.active_account)]))
        max_description_length = max(len("Description"), max(
            [len(task.description) for task in self.task_manager.get_tasks(self.account_manager.active_account)]))
        max_accounts_length = max([len(", ".join([account.name for account in task.accounts])) for task in
                                   self.task_manager.get_tasks(self.account_manager.active_account)])
        print("Nom".ljust(max_name_length) + " | " + "Description".ljust(
            max_description_length) + " | " + "Comptes".ljust(max_accounts_length) + " | " + "Complétée")
        for task in self.task_manager.get_tasks(self.account_manager.active_account):
            print(task.name.ljust(max_name_length) + " | " + task.description.ljust(
                max_description_length) + " | " + ", ".join([account.name for account in task.accounts]).ljust(
                max_accounts_length) + " | " + bool_to_str(task.done))


class ClearTasksCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("vider", account_manager, task_manager)

    def execute(self):
        self.task_manager.clear_tasks(self.account_manager.active_account)


class LoginCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("connecter", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        self.account_manager.connect(name)


class AddUserCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("ajouter-compte", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        can_manage_tasks = input("Peut gérer les tâches ? (o/n) : ").lower() == "o"
        can_manage_accounts = input("Peut gérer les comptes ? (o/n) : ").lower() == "o"
        self.account_manager.add_account(Account(name, can_manage_tasks, can_manage_accounts))


class DeleteUserCommand(Command):
    def __init__(self, account_manager, task_manager):
        super().__init__("supprimer-compte", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        self.account_manager.delete_account(self.account_manager.get_account(name))
        print("RIP {}, à jamais dans nos coeurs".format(name))


def bool_to_str(bool):
    if bool:
        return "Oui"
    return "Non"


def main():
    account_manager = AccountManager()
    task_manager = TaskManager()
    commands = [AddTaskCommand(account_manager, task_manager),
                DeleteTaskCommand(account_manager, task_manager),
                MarkTaskAsDoneCommand(account_manager, task_manager),
                ListTasksCommand(account_manager, task_manager),
                ClearTasksCommand(account_manager, task_manager),
                LoginCommand(account_manager, task_manager),
                AddUserCommand(account_manager, task_manager),
                DeleteUserCommand(account_manager, task_manager)
                ]
    print("Liste des commandes :")
    for command in commands:
        print(command.name)
    print("Pour quitter, tapez 'quitter'.")
    while True:
        command_name = input("Commande : ")
        found = False
        if command_name == "quitter":
            break
        for command in commands:
            if command.name == command_name:
                found = True
                try:
                    command.execute()
                except PermissionError as e:
                    print("Erreur : {}".format(e))
                except Exception as e:
                    print("Une erreur s'est produite lors de l'exécution de cette commande : {}".format(e))
                    print("Veuillez vérifier que vous avez entré les bonnes informations et réessayer.")
                finally:
                    break
        if not found:
            print("Commande inconnue.")


if __name__ == "__main__":
    main()

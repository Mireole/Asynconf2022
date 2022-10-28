# Mireole#8364
# Exercice 3 : Gérez vos tâches

class PermissionError(Exception):
    pass


class Account:
    """An account"""
    def __init__(self, name, can_manage_tasks, can_manage_users):
        self.name = name
        self.can_manage_tasks = can_manage_tasks
        self.can_manage_users = can_manage_users


class AccountManager:
    """Manages accounts."""
    def __init__(self):
        self.accounts = []
        self.accounts.append(Account("Administrateur", True, True))
        self.active_account = self.get_account("Administrateur")

    def add_account(self, account):
        """Add an account to the list of accounts."""
        if not self.active_account.can_manage_users:
            raise PermissionError("Vous n'avez pas la permission de gérer les comptes.")
        if [True for registered_account in self.accounts if registered_account.name == account.name]:
            raise ValueError("Le compte avec le nom {} existe déjà.".format(account.name))
        self.accounts.append(account)

    def delete_account(self, account):
        """Delete an account from the list of accounts."""
        if not self.active_account.can_manage_users:
            raise PermissionError("Vous n'avez pas la permission de gérer les comptes.")
        if account == self.active_account:
            raise ValueError("Vous ne pouvez pas supprimer votre propre compte.")
        if account == self.get_account("Administrateur"):
            raise ValueError("Pas de coups d'états.")
        self.accounts.remove(account)

    def get_account(self, name):
        """Get an account from the list of accounts from its name."""
        for account in self.accounts:
            if account.name == name:
                return account
        raise ValueError("Le compte avec le nom {} n'existe pas.".format(name))

    def connect(self, name):
        """Connect to an account."""
        self.active_account = self.get_account(name)


class Task:
    """A Simple Task class"""
    def __init__(self, name, description, accounts):
        self.name = name
        self.description = description
        self.accounts = accounts
        self.done = False

    def set_done(self):
        """Set the task as done."""
        self.done = True


class TaskManager:
    """Manages tasks."""
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list of tasks."""
        self.tasks.append(task)

    def get_tasks(self, account):
        """Get the list of tasks available to the user."""
        if account.can_manage_tasks:
            return self.tasks
        return [task for task in self.tasks if account in task.accounts]

    def delete_task(self, task_name, account):
        """Delete a task from the list of tasks."""
        if account.can_manage_tasks:
            self.tasks = [task for task in self.tasks if task.name != task_name]
        else:
            raise PermissionError("Vous n'avez pas la permission de gérer les tâches.")

    def clear_tasks(self, account):
        """Clear the list of tasks."""
        if account.can_manage_tasks:
            self.tasks = []
        else:
            raise PermissionError("Vous n'avez pas la permission de gérer les tâches.")


class Command:
    """A basic command class, inherited by all other commands."""
    def __init__(self, name, account_manager, task_manager):
        self.name = name
        self.account_manager = account_manager
        self.task_manager = task_manager

    def execute(self):
        """Execute the command."""
        pass


class AddTaskCommand(Command):
    """Add a task to the list of tasks."""
    def __init__(self, account_manager, task_manager):
        super().__init__("ajouter", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        description = input("Description de la tâche : ")
        accounts = input("Comptes associés (séparés par des virgules) : ").split(",")
        for i in range(len(accounts)):
            accounts[i] = self.account_manager.get_account(accounts[i])
        self.task_manager.add_task(Task(name, description, accounts))
        print("Tâche ajoutée.")


class DeleteTaskCommand(Command):
    """Delete a task from the list of tasks."""
    def __init__(self, account_manager, task_manager):
        super().__init__("retirer", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        self.task_manager.delete_task(name, self.account_manager.active_account)
        print("Tâche retirée.")


class MarkTaskAsDoneCommand(Command):
    """Mark a task as done."""
    def __init__(self, account_manager, task_manager):
        super().__init__("compléter", account_manager, task_manager)

    def execute(self):
        name = input("Nom de la tâche : ")
        for task in self.task_manager.get_tasks(self.account_manager.active_account):
            if task.name == name:
                task.set_done()
                print("Tâche complétée.")
                return
        raise ValueError("La tâche {} n'existe pas ou vous n'y avez pas accès.".format(name))


class ListTasksCommand(Command):
    """List the tasks available to the user."""
    def __init__(self, account_manager, task_manager):
        super().__init__("liste", account_manager, task_manager)

    def execute(self):
        if not self.task_manager.get_tasks(self.account_manager.active_account):
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
    """Clear the list of tasks."""
    def __init__(self, account_manager, task_manager):
        super().__init__("vider", account_manager, task_manager)

    def execute(self):
        self.task_manager.clear_tasks(self.account_manager.active_account)
        print("Tâches vidées.")


class LoginCommand(Command):
    """Login to an account."""
    def __init__(self, account_manager, task_manager):
        super().__init__("connecter", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        self.account_manager.connect(name)
        print("Connecté en tant que {}.".format(name))


class AddUserCommand(Command):
    """Add a user to the list of users."""
    def __init__(self, account_manager, task_manager):
        super().__init__("ajouter-compte", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        can_manage_tasks = input("Peut gérer les tâches ? (o/n) : ").lower() == "o"
        can_manage_accounts = input("Peut gérer les comptes ? (o/n) : ").lower() == "o"
        self.account_manager.add_account(Account(name, can_manage_tasks, can_manage_accounts))
        print("Compte ajouté.")


class DeleteUserCommand(Command):
    """Delete a user from the list of users."""
    def __init__(self, account_manager, task_manager):
        super().__init__("supprimer-compte", account_manager, task_manager)

    def execute(self):
        name = input("Nom du compte : ")
        self.account_manager.delete_account(self.account_manager.get_account(name))
        print("RIP {}, à jamais dans nos coeurs".format(name))


def bool_to_str(bool):
    """Convert a boolean to a french yes / no (oui / non)."""
    if bool:
        return "Oui"
    return "Non"


def main():
    """Main function."""
    # Initialize the managers
    account_manager = AccountManager()
    task_manager = TaskManager()
    # All commands available
    commands = [AddTaskCommand(account_manager, task_manager),
                DeleteTaskCommand(account_manager, task_manager),
                MarkTaskAsDoneCommand(account_manager, task_manager),
                ListTasksCommand(account_manager, task_manager),
                ClearTasksCommand(account_manager, task_manager),
                LoginCommand(account_manager, task_manager),
                AddUserCommand(account_manager, task_manager),
                DeleteUserCommand(account_manager, task_manager)
                ]
    # Print the list of commands
    print("Liste des commandes :")
    for command in commands:
        print(command.name)
    print("Pour quitter, tapez 'quitter'.")
    # Main loop
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

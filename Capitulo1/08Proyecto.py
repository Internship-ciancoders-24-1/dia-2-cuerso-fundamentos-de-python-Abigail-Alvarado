
clients = 'pablo, ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _addComa()
    else:
        print('Client already in the client\'s list')

def listClients():
    global clients
    print(clients)

def _addComa():
    global clients
    clients += ','   

def __printWelcome():
    print('WELCOME TO PLAZTI VENTAS')
    print('*' * 50)
    print('What would you like to do today')
    print('[C]reate client')
    print('[D]elete client')

if __name__ == '__main__':
    __printWelcome()
    command = input()

    if command == 'C':
        client_name = input('What is the client name: ')
        create_client(client_name)
        listClients()
    elif command == 'D':
        pass
    else:
        print('invalid command')
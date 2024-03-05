import sys


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

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name)
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')

def searchClient(client_name):
    clients_list = clients.split(',')

    for Client in clients_list:
        if Client != client_name:
            continue
        else:
            return True


def __printWelcome():
    print('WELCOME TO PLAZTI VENTAS')
    print('*' * 50)
    print('What would you like to do today')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')

def _getClientName():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
            sys.exit()   


    return client_name      

if __name__ == '__main__':
    __printWelcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _getClientName()
        create_client(client_name)
        listClients()
    elif command == 'D':
        client_name = _getClientName()
        delete_client(client_name)
        listClients()
    elif command == 'U':
        client_name = _getClientName()
        updated_client_name = input('What is the updated client name ')
        update_client(client_name, updated_client_name)
        listClients()
    elif command == 'S':
        client_name = _getClientName()
        found = searchClient(client_name)

        if found:
            print('The client is un the client\'s list')
        else:
           print('The client: {} is not in our client\'s list'.format(client_name))      
    else:
        print('invalid command')
import sys


clients = [
    {
        'name':'Pablo',
        'company':'Google',
        'gmail':'pablo@google.com',
        'position':'software engineer',
    },
    {
        'name':'Ricardo',
        'company':'Google',
        'gmail':'Ricardo@google.com',
        'position':'software engineer',
    }


]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')

def listClients():
    for idx, client in enumerate(clients):
        print('{uid} |{name} | {company} | {gmail} |{position} '.format(
            uid =idx,
            name=client['name'],
            company=client['company'],
            gmail=client['gmail'],
            position=client['position'],
        ))

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    for client in clients:
        if client['name'] == client_name:
            clients.remove(client)
            return
    print('Client is not in clients list')

def searchClient(client_name):
    for client in clients:
        if client['name'] == client_name:
            return True
    return False

def __printWelcome():
    print('WELCOME TO PLAZTI VENTAS')
    print('*' * 50)
    print('What would you like to do today')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')
    print('[L]ist client')

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

def _getClientField(field_name):
    field = None 

    while not field:
        field = input('What is the client {} ? '.format(field_name))

    return field 

if __name__ == '__main__':
    __printWelcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name':_getClientField('name'),
            'company':_getClientField('company'),
            'email':_getClientField('email'), 
            'position':_getClientField ('position')                      
        }
        create_client(client)
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
    elif command == 'L':
        listClients()           
    else:
        print('invalid command')
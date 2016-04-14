# python2
# Create empty dictionary with contacts
contacts = {}

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(raw_input())
    return [Query(raw_input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def findContact(number):
    if number in contacts:
        return contacts[number]
    else:
        return None

def deleteContact(number):
    # If entry doesn't exist pop will return None
    # so no need for try - except
    contacts.pop(number, None)

def addContact(name, number):
    # This will either add a new entry or update the existing one
    contacts[number] = name

def process_queries(queries):
    result = []
    for cur_query in queries:
        number = cur_query.number
        if cur_query.type == 'add':
            name = cur_query.name
            addContact(name, number)
        elif cur_query.type == 'del':
            deleteContact(number)
        else:
            response = findContact(number)
            if response ==  None:
                response = "not found"
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

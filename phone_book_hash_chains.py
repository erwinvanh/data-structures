# python2
contacts = {}
a = 43
b = 3
p = 10**7 + 3
m = 1000

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

def createDict():
    for i in range(m):
        contacts[i] = {}

def hashNumber(number):
    return (( a * number + b) % p ) % m

def findContact(number, hashedNumber):
    if number in contacts[hashedNumber]:
        return contacts[hashedNumber][number]
    else:
        return None

def deleteContact(number, hashedNumber):
    # If entry doesn't exist pop will return None
    # so no need for try - except
    contacts[hashedNumber].pop(number, None)

def addContact(name, number, hashedNumber):
    # This will either add a new entry or update the existing one
    contacts[hashedNumber][number] = name

def process_queries(queries):
    result = []
    createDict()

    for cur_query in queries:
        number = cur_query.number
        hashedNumber = hashNumber(number)
        if cur_query.type == 'add':
            name = cur_query.name
            addContact(name, number, hashedNumber)
        elif cur_query.type == 'del':
            deleteContact(number, hashedNumber)
        else:
            response = findContact(number, hashedNumber)
            if response ==  None:
                response = "not found"
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


DATA = """name,age,dni
Juan,30,1057835308
Steven,25,1095953
Karol,18,10973400
"""

def convertToJson():    
    collection = []

    # with open('./assets/test.csv', 'r') as file:
        # content = file.read().split('\n')
        
    content = DATA.split('\n')

    headers = content[0]
    data = content.copy()
    data.pop(0)

    for row in data:
        new_record = {}

        for key, value in zip(headers.split(','), row.split(',')):
            new_record.update({f'{key}': f'{value}'})
            
        collection.append(new_record)
    
    print(collection)
    return collection            

convertToJson()

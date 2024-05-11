def clean_data(
    data_path: str = ..., 
    save_path: str = ...
) -> str:

    print(' - Cleaning data')

    ### load data to be cleaned
    with open(data_path, 'r') as file:
        content = file.read().split('\n')

        headers = content[0]
        data = content.copy()
        data.pop(0)
        data = "\n".join(data)
    
    ### Deleting comma (,) char from names
    comma_names = ''
    for i in data.split('"'):
        if len(i) > 100:
            comma_names += i
        else:
            comma_names += i.replace(',', '')
    data = comma_names

    ### Deleting extra chars
    data = data.replace('\n', ';')
    data = data.replace(', ', ',')
    data = data.replace(' ,', ',')
    data = " ".join(data.split())
    data = data.replace('.0,', ',')
    data = data.replace('"', '')
    data = data.replace('`', '')
    data = data.replace(';', '\n')

    ### Save cleaned data
    with open(save_path, 'w') as file:
        file.write(data)

    return data
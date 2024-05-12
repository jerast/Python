def clean_data(
    data_path: str = ..., 
    save_path: str = ...
) -> None:

    print(' - Cleaning data')

    ### Load data to be cleaned
    with open(data_path, 'r') as file:
        file_content = file.read().split('\n')
        headers = file_content.pop(0)
        data = '\n'.join(file_content)

    ### Delete extra chars:
    # decimals in int values
    data = data.replace('.0;', ';') 
    # extra commas
    data = data.replace(',', '')
    # double spaces at start and end of any cell
    data = data.replace('; ', ';')
    data = data.replace(' ;', ';')
    # double spaces at middle of any cell
    data = data.replace('\n', '_')
    data = ' '.join(data.split())
    data = data.replace('_', '\n')
    # extra quotation marks
    data = data.replace('"', '')
    
    ### Set CSV default separator
    headers = headers.replace(';', ',')
    data = data.replace(';', ',')

    ### Save cleaned data
    with open(save_path, 'w') as file:
        file.write( headers+'\n'+data )
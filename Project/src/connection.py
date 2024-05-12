import pyodbc
import pandas
import warnings
from config import DRIVER, SERVER, DATABASE, USERNAME, PASSWORD


def get_data(
    sql_path: str = ..., 
    save_path: str = ...
) -> None:
    print(' - Fetching data')

    ### Establishing the connection
    connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=YES;'
    connection = pyodbc.connect(connectionString)
    
    ### Suprime pandas warning
    warnings.filterwarnings('ignore', category=UserWarning)

    ### Excecute query with pandas
    query = pandas.read_sql_query(
        get_query_from_file(sql_path),
        connection,
    )

    ### Get query data and save in .CSV file
    results = pandas.DataFrame(query)
    results.to_csv(save_path, index=False, header=True, sep=";")

def get_query_from_file(file_path):
    with open(file_path) as file:
        content = file.read()

    return '' if not content else content

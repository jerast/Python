import sys
import os
import pandas
import numpy
import matplotlib
import matplotlib.pyplot as pyplot
import seaborn
from src import connection, cleaner, filter


MD = sys.path[0]

def main() -> None:
    os.system('clear')
    
    prepare_data(fetched=True)

def prepare_data(
    fetched: bool = True
) -> None:

    print('Preparing Data...')
    
    ### Getting data from DB
    if not fetched:
        connection.get_data(
            sql_path=MD+'/assets/query.sql',
            save_path=MD+'/assets/data.csv'
        )

    ### Cleaning data
    cleaner.clean_data(
        data_path=MD+'/assets/data.csv',
        save_path=MD+'/assets/data_cleaned.csv'
    )

    ### Filtering data
    filter.filter_data(
        data_path=MD+'/assets/data_cleaned.csv',
        save_path=MD+'/assets/data_filtered.csv',
        time_range='D', # [Y, M, D]
        filter='modelo', # [asesor, modelo, clasificacion]
        values='cantidad' # [cantidad, costo]
    )
 
main()

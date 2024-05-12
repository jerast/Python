import sys
from src import connection, cleaner, filter


MD = sys.path[0]

def main() -> None:
    prepare_data()

    print('Done!')

def prepare_data() -> None:
    print('Preparing Data...')
    
    ### Getting data from DB
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
        save_path=MD+'/assets/filter.json',
        time_range='Y', # [Y, M, D]
        filter='des_modelo', # [nom_asesor, des_modelo, financiera, clasificacion]
        values='costo', # [cantidad, costo]
        order_by='values', # [keys, values]
        desc=True,
        accum=True,
        invert=False,
    )
 
main()

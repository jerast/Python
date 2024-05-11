import sys
from src import connection, cleanner, filter, export

MD = sys.path[0]

def main() -> None:
    prepare_data()

    print('\nDone!\n')

def prepare_data() -> None:
    print('\nPreparing Data...\n')
    
    ### Getting data from DB
    connection.get_data(
        sql_path=MD+'/assets/query.sql',
        save_path=MD+'/assets/data.csv'
    )

    ### Cleaning data
    cleanner.clean_data(
        data_path=MD+'/assets/data.csv',
        save_path=MD+'/assets/data_cleaned.csv'
    )

    ### Filtering data
    filtered_data=filter.filter_data(
        data_path=MD+'/assets/data_cleaned.csv',
        time_range='Y', # [Y, M, D]
        filter='modelo', # [asesor, modelo, financiera, clasificacion]
        values='cantidad', # [cantidad, costo]
        order_by='valor', # [llave, valor]
        desc=True,
        accum=True,
        invert=False,
    )
        
    ### Exporting filtered data
    export.export_filter_data(
        filtered_data=filtered_data,
        export_path=MD+'/assets/filter.json'
    )

main()

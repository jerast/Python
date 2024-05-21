import pandas
from src.helpers.args_validator import args_verifier

validateParams = {
    'time_range': ['Y', 'M', 'D'], 
    'filter': ['asesor', 'modelo', 'clasificacion'], 
    'values': ['cantidad', 'costo'], 
}
@args_verifier(validateParams)
def filter_data(
    data_path: str = ..., 
    save_path: str = ...,
    time_range: str = ...,
    filter: str = ...,
    values: str = ...,
) -> None:

    print(f""" - filtering data:
    get `{values}` 
    per `{filter}` 
    with time `{time_range}`""")

    # Load data to be filtered
    filter_data = pandas.read_csv(data_path)
    
    # Set 'fecha' column as 'datetime' type
    filter_data['fecha'] = pandas.to_datetime(filter_data['fecha'], format="%Y-%m-%d")

    # Delete unnecesary columns
    filter_data = filter_data.drop(columns=['sw', 'bodega', 'ident_asesor', 'ident_cliente', 'nom_cliente', 'utilidad', 'modelo', 'financiera', 'dias_inv', 'doc_ref'])

    # Create params maps
    date_mappings = {
    'Y': {
        'symbol': 'YE',
        'format': '%Y'
    },
    'M': {
        'symbol': 'ME',
        'format': '%Y-%m'
    },
    'D': {
        'symbol': 'D',
        'format': '%Y-%m-%d'
    }
    }
    filter_mappings = {
        'asesor': 'nom_asesor',
        'modelo': 'des_modelo',
        'financiera': 'financiera',
        'clasificacion': 'clasificacion'
    }
    values_mappings = {
        'cantidad': {
            'name': 'cantidad',
            'type': int
        },
        'costo': {
            'name': 'costo_unitario',
            'type': float
        }
    }

    # Set the variables according params
    selected_time = date_mappings.get(time_range)
    selected_filter = filter_mappings.get(filter)
    selected_value = values_mappings.get(values)

    # Group dataframe by ['fecha'] as primary and [selected_filter] as secondary
    data_group = filter_data.groupby(
        [pandas.Grouper(key='fecha', freq=selected_time['symbol'], sort=True), selected_filter]
    )[selected_value['name']].sum() 
    
    # Convert group series in a new dataframe
    data_filtered = data_group.unstack(level=1)
    data_filtered = data_filtered.fillna(0)
    data_filtered = data_filtered.astype(selected_value['type'])
    data_filtered.index = data_filtered.index.strftime(selected_time['format'])

    # Export filtered_data
    data_filtered.to_csv(save_path, date_format=selected_time['format'])
    data_filtered.to_json(save_path.replace('.csv', '.json'), date_format=selected_time['format'], indent=3)

    
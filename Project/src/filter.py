import json
from src.helpers.args_validator import args_verifier

validateParams = {
    'time_range': ['Y', 'M', 'D'], 
    'filter': ['nom_asesor', 'des_modelo', 'financiera', 'clasificacion'], 
    'values': ['cantidad', 'costo'], 
    'order_by': ['keys', 'values'],
}
@args_verifier(validateParams)
def filter_data(
    data_path: str = ..., 
    save_path: str = ...,
    time_range: str = ...,
    filter: str = ...,
    values: str = ...,
    invert: bool = False,
    order_by: str = ...,
    desc: bool = False,
    accum: bool = False
) -> None:

    print(f""" - filtering data:
    get `{values}` 
    per `{filter}` 
    sorted by `obj.{order_by}` {'desc' if desc else 'asc'}
    with time `{time_range}`
    with {'accum' if accum else 'no accum'}
    with {'inverted' if invert else 'normal'} orientation""")


    ### Set init values, empty data and time-range separator
    filtered_data = {}
    selected_datetime = ['Y','M','D'].index(time_range)

    ### Get data from file
    with open(data_path, 'r') as original_data:
        
        ### Remove headers
        data = original_data.read().split('\n')
        data.pop(0)

        for row in data:
            try:
                record = row.split(',')

                ### Get all needed values from row. filters and values
                date = record[2].split('-')
                filter_mappings = {
                    'nom_asesor': record[4],
                    'des_modelo': record[11],
                    'financiera': record[12],
                    'clasificacion': record[14]
                }
                values_mappings = {
                    'cantidad': int(record[7]),
                    'costo': float(record[9])
                }

                ### Set the variables according to the parameters
                selected_range = "-".join(date[:selected_datetime+1])
                selected_filter = filter_mappings.get(filter)
                selected_value = values_mappings.get(values)

                x_var = selected_range if not invert else selected_filter
                y_var = selected_filter if not invert else selected_range

                ### Set the filtered_data Keys and Values
                if filtered_data.get(x_var) is None:
                    filtered_data[x_var] = {}
                    filtered_data[x_var][y_var] = selected_value
                else:
                    if filtered_data[x_var].get(y_var) is None:
                        filtered_data[x_var][y_var] = selected_value
                    else:
                        filtered_data[x_var][y_var] += selected_value

                if accum:
                    if filtered_data[x_var].get('_TOTAL_') is None:
                        filtered_data[x_var]['_TOTAL_'] = selected_value
                    else:
                        filtered_data[x_var]['_TOTAL_'] += selected_value

            ### If any cell has parse errors, print entire row and break the for Cycle
            except:
                print(row)
                break


    ### Sorted dict according params
    for key in filtered_data:
        if order_by == 'llave':
            filtered_data[key] = dict(sorted(filtered_data[key].items(), reverse=desc))
        if order_by == 'valor':
            filtered_data[key] = dict(sorted(filtered_data[key].items()))
            filtered_data[key] = dict(sorted(filtered_data[key].items(), key=lambda x:x[1], reverse=desc))
    
    filtered_data = dict(sorted(filtered_data.items()))

    ### Exporting filtered data
    export_filter_data(
        filtered_data=filtered_data,
        export_path=save_path
    )

def export_filter_data(
    filtered_data: str = ..., 
    export_path: str = ...,
) -> None:
    
    filter_file = open(export_path, 'w')

    json.dump(
        filtered_data, 
        filter_file, 
        indent=4,
        ensure_ascii=False
    )

    filter_file.close()
    
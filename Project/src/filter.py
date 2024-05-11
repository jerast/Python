from src.helpers.validators import valores_permitidos_filter as verifier

validateParams = {
    "time_range": ["Y", "M", "D"], 
    "filter": ["asesor", "modelo", "financiera", "clasificacion"], 
    "values": ["cantidad", "costo"], 
    "order_by": ["llave", "valor"],
}
@verifier(validateParams)
def filter_data(
    data_path: str = ..., 
    time_range: str = ..., 
    filter: str = ...,
    values: str = ...,
    invert: bool = False,
    order_by: str = ...,
    desc: bool = False,
    accum: bool = False
) -> dict:

    print(f""" - filtering data:\n
    get `{values}` 
    per `{filter}` 
    sorted by `{order_by}` {'desc' if desc else 'asc'}
    with time `{time_range}`
    with {'accum' if accum else 'no accum'}
    with {'inverted' if invert else 'normal'} orientation
    """)

    filtered_data = {}
    selected_datetime = ['Y','M','D'].index(time_range)

    with open(data_path, 'r') as data:

        for row in data:
            record = row.split(',')

            date = record[3].split('-')
            filter_mappings = {
                'asesor': record[5],
                'modelo': record[12],
                'financiera': record[13],
                'clasificacion': record[15]
            }
            values_mappings = {
                'cantidad': int(record[8]),
                'costo': float(record[10])
            }

            selected_range = "-".join(date[:selected_datetime+1])
            selected_filter = filter_mappings.get(filter)
            selected_value = values_mappings.get(values)

            x_var = selected_range if not invert else selected_filter
            y_var = selected_filter if not invert else selected_range

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

    for key in filtered_data:
        if order_by == 'llave':
            filtered_data[key] = dict(sorted(filtered_data[key].items(), reverse=desc))
        if order_by == 'valor':
            filtered_data[key] = dict(sorted(filtered_data[key].items()))
            filtered_data[key] = dict(sorted(filtered_data[key].items(), key=lambda x:x[1], reverse=desc))
    
    filtered_data = dict(sorted(filtered_data.items()))

    return filtered_data
    


    
import json

def export_filter_data(
    filtered_data: str = ..., 
    export_path: str = ...,
) -> None:
    
    # print(' - Exporting filter data')

    filter_file = open(export_path, 'w')

    json.dump(
        filtered_data, 
        filter_file, 
        indent=4,
        ensure_ascii=False
    )

    filter_file.close()
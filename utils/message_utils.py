def MessageFilter(data,source_data):
    # Modify after_data by joining with source_data
    if source_data:
        data.update(source_data)
    
    # Remove specific items from after_data dictionary
    items_to_remove = ['req_code','req_resp_code', 'money_valid_code', 'check_code', 'check_resp_code','callback_code','certify_resp_code']
    for item in items_to_remove:
        data.pop(item, None)

    data = {key: value.replace(' ', '').replace('\n', '') if isinstance(value, str) else value for key, value in data.items()}
    
    return data
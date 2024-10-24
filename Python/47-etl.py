def transform(legacy_data):
    new_data = {}
    
    for key, list in legacy_data.items():
        for i in list:
            new_data[i.lower()] = key

    return new_data

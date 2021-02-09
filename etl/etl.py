def transform(legacy_data):
    rev_data = {
        value.lower(): key for key, values in legacy_data.items() for value in values
    }

    return rev_data


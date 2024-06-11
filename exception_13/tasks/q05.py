def fetch_element(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return 'key not found in the dictionary!'


v_result = fetch_element({'a': 1, 'b': 2}, 'c')
print(v_result)
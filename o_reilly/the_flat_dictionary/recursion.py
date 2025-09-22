def flatten(dictionary):
    flatten_dict = {}

    for k in dictionary:
        if not isinstance(dictionary[k], dict):
            flatten_dict[k] = dictionary[k]
        elif len(dictionary[k]) == 0:
            flatten_dict[k] = ''
        else:
            nested_dict = flatten(dictionary[k])
            for i in nested_dict:
                flatten_dict[f'{k}/{i}'] = nested_dict[i]

    return flatten_dict

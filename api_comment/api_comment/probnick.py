data_dict = {'post': 1,
        'comment': 'i comment_1_2_3',
        'children': [{'post': 1,
                      'comment': 'i comment_1_2_3_4',
                      'children': [{'post': 1,
                                    'comment': 'i comment_1_2_3_4_5',
                                    'children': []}]}]}


def filter_data(data, val):

    counter = 0
    if isinstance(data, dict):
        for value_dict in data:
            if value_dict == val:
                counter += 1
                sum_count = filter_data(data[value_dict], val)
                counter += sum_count
    elif isinstance(data, list):
        for value_list in data:
            counter = filter_data(value_list, val)
    return counter


print(filter_data(data_dict, 'children'))
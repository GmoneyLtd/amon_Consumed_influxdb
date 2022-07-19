import pysnooper

str = {'rows': 2, 'columns': ['a', 'b', 'c'], 'data': [[1, 2, 3], [4, 5, 6]]}


@pysnooper.snoop()
def amon2dict(amon: str) -> dict:
    # amon_dict = json.loads(amon)
    amon_dict = amon
    print(amon_dict)
    msg_dict = {}

    msg_dict['name'] = amon_dict.get('name')
    msg_dict['type'] = amon_dict.get('type')
    # msg_dict['major']=amon_dict.get('major')
    # msg_dict['minor']=amon_dict.get('minor')
    msg_dict['timestamp'] = amon_dict.get('timestamp')
    msg_dict['sequence'] = amon_dict.get('sequence')
    msg_dict['source'] = amon_dict.get('source')
    msg_dict['data'] = []

    row_num = 0
    while row_num < amon_dict.get('rows'):
        index = 0
        temp_val = {}
        for column_name in amon_dict.get('columns'):
            temp_val[column_name] = amon_dict.get('data')[row_num][index]
            index += 1
        msg_dict['data'].append(temp_val)
        row_num += 1

    return msg_dict


if __name__ == '__main__':
    res = amon2dict(str)
    print(res)

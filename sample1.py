

if __name__ == '__main__':
    print('hellow world')

    total = 1.0
    temp = 'string value'

    if total > 50:
        print('lebih besar dari 50')
    else:
        print('lebih keci dari 50')

    values = [11,21,33,45,57,6]
    values = list()
    print(values)
    values.append(100)
    print(values)

    for data in values:
        print(data)

    profile = {
        'name' : 'hendri',
        'alamat' : 'bandung barat',
        'hobi' : 'makan'
    }

    print(profile)

    print()
    print(profile['name'])
    print(profile['alamat'])
    print('+++++++++++++')

    for key, value in profile.items():
        print(key)
        print(value)
        print('------------')


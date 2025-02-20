while True:
    ip_address = input('Введите IP: ').split('.')

    if len(ip_address) < 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        num = 0
        out = 0
        for item in ip_address:
            if item.isdigit():
                num += 1
                if int(item) > 255:
                    out += 1
                    print('{} превышает 255'.format(item))
            else:
                print('{} — это не целое число.'.format(item))

        if out == 0 and num == 4:
            print('IP-адрес корректен.')
            break




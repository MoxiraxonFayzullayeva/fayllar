
store =[]
while True:
    command = input('Command:')
    if command == '/add':
        store.append(
            {
                'name': input('Nomini kiriting: ')
                'narxi': int(input('Narxini kiriting: '))
                'soni': int(input('Miqdori kiriting: '))
            }
        )

    elif command == '/royxat':
        for i in store:
            print(f'{i["name"]} - {i["narxi"]} so\'m, {i["soni"]}ta')


    elif command == '/exit':
        print("Xaridingiz uchun tashakkur!")
        break

    # else:
    #     if buyurtma in ['stop', 'exit']:
    #         for k, v in client.items():
    #             print(f'{k.upper()} ---------------------- {v} so\'m.')
    #         print(f"\nUMUMIY HISOB: {hisob} so'm.")
    #         break
    #     else:
    #         print("Bunday taom mavjud emas!")






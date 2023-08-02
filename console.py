import tdb

splash = '''  _______ _     _                 _                 
 |__   __| |   | |               (_)                
    | |  | |__ | |__   ___  _ __  _  ___ __ _ _ __  
    | |  | '_ \| '_ \ / _ \| '_ \| |/ __/ _` | '_ \ 
    | |  | | | | |_) | (_) | |_) | | (_| (_| | | | |
  __|_|  |_| |_|_.__/ \___/| .__/|_|\___\__,_|_| |_|
 |  __ \      | |      | | | |                      
 | |  | | __ _| |_ __ _| |_|_| __ _ ___  ___        
 | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \       
 | |__| | (_| | || (_| | |_) | (_| \__ \  __/       
 |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|       
  / ____|                    | |                    
 | |     ___  _ __  ___  ___ | | ___                
 | |    / _ \| '_ \/ __|/ _ \| |/ _ \               
 | |___| (_) | | | \__ \ (_) | |  __/               
  \_____\___/|_| |_|___/\___/|_|\___|               
                                                    
                                                    


'''

print(splash)

db = None
while True:
    cmd = input('--> ').split(' ')
    
    if cmd[0] == 'quit':
        print('Quitting')
        break

    elif cmd[0] == 'help':
        print('Nothing here for now')

    elif cmd[0] == 'set':
        if cmd[1] == 'db':
            db = tdb.Database(cmd[2])
            print(f'Database set to "{cmd[2]}"')

    elif cmd[0] == 'get':
        if cmd[1] == 'db':
            if db == None:
                print('Database currently not set')
            else:
                print(f'Database open "{db.file.base}"')
    
    elif cmd[0] == 'db':
        if db != None:
            if cmd[1] == 'set':
                if cmd[2] == 'dict':
                    db.data[cmd[3]] = {}
                elif cmd[2] == 'list':
                    db.data[cmd[3]] = []
                db.save()
            
            elif cmd[1] == 'get':
                try:
                    print(db.data[cmd[2]])
                except KeyError:
                    print(f'"{cmd[2]}" not found in "{db.file.base}"')
            
            elif cmd[1] == 'getall':
                if len(db.data) == 0:
                    print('No keys in database')
                else:
                    print('Keys in database:')
                    for k in db.data:
                        print('\t' + k)
                    print()
            
            elif cmd[1] == 'remove':
                try:
                    if input('Confirm (y/n): ') == 'y':
                        db.data.pop(cmd[2])
                        print(f'"{cmd[2]}" removed sucessfully from "{db.file.base}"')
                    else:
                        print('Cancelled')
                except KeyError:
                    print(f'"{cmd[2]}" not found in "{db.file.base}"')
                db.save()
        else:
            print('Make sure to set your database file\nset db <file.tdb>')
    
    else:
        print(f'Unrecognized command: "{cmd[0]}"\nType "help" for help')
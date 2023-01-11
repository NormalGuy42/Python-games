def Tamagotchi():
    state = 'HAPPY'
    hungry = 0
    bored = 0

    while True: 
        msg = input(f'Tamagotchi current state: {state}\n')
        #feed, play, ignore
        if msg == 'feed':
            bored += 1
            if hungry>=0: hungry -=1
            else: hungry = 0
        elif msg == 'play':
            hungry +=1
            if bored>=0: bored -=1
            else: bored= 0
        elif msg == 'ignore':
            hungry+= 1
            bored += 1

        #Change states
        if state == 'HAPPY':
            if bored>= 2: state ='BORED'
            elif hungry>= 2: state = 'HUNGRY'
        elif state == 'HUNGRY':
            if bored >= 4: state = 'SAD'
            elif bored > hungry: state = 'BORED'
            elif hungry < 2: state = 'HAPPY'
        elif state == 'BORED':
            if bored >= 4: state = 'SAD'
            elif hungry > bored: state = 'HUNGRY'
            if bored < 2: state = 'HAPPY'

        if state == 'SAD':
            break
            
    print('You made your Tamagotchi sad')   

        

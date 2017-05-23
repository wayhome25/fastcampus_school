champion = 'Lux'

def show_global_champion():
    print('show_global_champion: {}'.format(champion))

def change_global_champion():
    #print('before_chage:{}'.format(champion))
    champion = 'Hi'
    print('local scope champion id: {}'.format(id(champion)))
    print('before_chage:{}'.format(champion))
show_global_champion()
change_global_champion()
print('print_champion:{}'.format(champion))
print('print_champion id: {}'.format(id(champion)))


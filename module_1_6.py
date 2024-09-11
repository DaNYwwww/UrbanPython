
my_dict = {'Daniil':2005 , 'Kirill': 2000, 'Elizaveta': 2004}
print("Dict:",my_dict)
print("Existing value:",my_dict.get('Daniil'))
print('No exciting value:',my_dict.get('Barbara'))
my_dict.update({'Maksim': 1999, 'Eva': 2010})
a = my_dict.pop('Kirill')
print('Delete value:', a)
print("New dict:", my_dict)

my_set = {1,1,1,1,1,1,2,3,3,"Love","Love","Death","Robots",True, (1,2,3),(1,2,3),(11,22,33)}
print("Set:",my_set)
my_set.add('5')
my_set.add(5.1)
my_set.remove((1,2,3))#or we can use mu_set.discard
print("New set:", my_set)

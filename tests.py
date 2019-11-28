from ssantav4 import*

def test_list_generator():
    names = ['Max', 'Raefe', 'Fred']
    assert len(list_generator(names)) == 3
    assert type(list_generator(names)) == list

def test_dictionary_maker():
    list_1 = ['Max', 'Raefe', 'Fred']
    list_2 = list_1
    assert type(dictionary_maker(list_1, list_2)) == dict
    assert (dictionary_maker(list_1, list_2))['Raefe'] == 'Raefe'

def test_duplicate_free():
    test_dict = {'Max':'Raefe','Raefe':'Fred','Fred':'Max'}
    assert duplicate_detector(test_dict) == False

def test_secret_santa():
    names = ['Max', 'Raefe', 'Fred']
    assert type(secret_santa(names)) == dict
    assert len(secret_santa(names)) == 3
    assert secret_santa(names)['Max'] != 'Max'



test_list_generator()
test_dictionary_maker()
test_duplicate_free()
print('Tests Passed.')
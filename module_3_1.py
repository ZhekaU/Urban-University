calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return len (tuple (string)), string.upper(), string.lower()
print(string_info('Новосибирск'))
print(string_info('Столица мира '))

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [string.lower() for string in list_to_search]
    return string in list_to_search
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

#parameter: used when defining a function i.e. placeholder for an argument
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
#arguments: used when calling a function
greet('en')
greet('es')
greet('fr')
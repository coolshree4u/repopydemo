passerby_speech='Hello'

if passerby_speech == 'Hello':
    print("Hello how are you ????")
elif passerby_speech=='hi':
    print("Hi How are you????")
else:
    print("Hey")


"""
Ternary operator demo
"""

me = "Hi" if passerby_speech =='Hi' or passerby_speech=='Hello' else "Hey"
print(me)


a=3

a =7 if 3**3 >9 else 14
print(a)
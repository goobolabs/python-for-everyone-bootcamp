name = input('please inter your name: ')
print('welcome, dear/darling: ', name)

score=0

q1 = input('q1: what is the capital city of Somalia? ')
q2 = input('q2: does Muqdisho has a beach? ')
q3= input('q3: what kind of city is Garoowe? ')
q4= input('q4: the most beutiful city in Somalia? ')

if(q1.lower() == 'muqdisho'):
    score += 1
if(q2.lower() == 'yes'):
    score += 1
if(q3.lower() == 'attractive city'):
    score += 1
if(q4.lower() == 'xaafuun'):
    score += 1

print('wow, you scored ', score, ' out of 4')

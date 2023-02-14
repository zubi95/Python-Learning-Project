# provience = input('What provience do you live in? ')
# tax = 0
# if provience.lower() in('auckland','napier','otago'):
#     tax = 0.05

# # if provience.lower() == 'auckland' or provience.lower() == 'napier':
# #     tax = 0.05
# elif provience.lower() == 'hamilton':
#     tax = 0.08
# elif provience.lower() == 'wellington':
#     tax = 0.07
# else:
#     tax = 0.15

country = input('What country do you live in? ')

if country.lower() == 'newzealand':
    provience = input('What provience do you live in? ')
    if provience.lower() in('auckland','napier','otago'):
        tax = 0.05
    elif provience.lower() == 'hamilton':
        tax = 0.08
    else:
        tax = 0.15
else:
    tax = 0.0

print(tax)
import shelve

db = shelve.open('data/t0txt')

num_qot = 0
num_not = 0

for key, value in db.items():
    content = value.lower()

    if 'qot' in content:
        num_qot += 1
    else:
        num_not += 1

print('num qot:', num_qot)
print('num not:', num_not)

print('ratio:', num_qot / len(db))
print('Qot.')

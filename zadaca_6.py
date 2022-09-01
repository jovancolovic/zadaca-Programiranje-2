import re

regex = '^(ime[a-z]).(prezime[a-z]).@.fpmoz.sum.ba.$'

regex2 = '^(i[a-z]).(prezime[a-z]).(x[]).@.sum.ba .$ '

while 1:
    email = input("unesite mail u formatu ime.prezime@fpmoz.sum.ba")

    result = re.match(regex,email)

    if result:
        break
print("uspjesan unos")

while 1:
    eduid = input("unesite mail u formatu i.prezimeX@fpmoz.sum.ba")

    result = re.match(regex2,eduid)

    if result:
        break
print("uspjesan unos")

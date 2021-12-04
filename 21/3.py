a = ["a","b","c","d","e"]
def kek():
    for t in a:
        yield t
c = kek()
for i in c:
    print(i)

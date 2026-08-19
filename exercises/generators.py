def gerade_zahlen(max_wert):
    for i in range(max_wert):
        if i % 2 == 0:             
            yield i    

for zahl in gerade_zahlen(10):
    print(zahl)
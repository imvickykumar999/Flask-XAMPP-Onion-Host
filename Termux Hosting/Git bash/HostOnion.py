
with open('HostOnion', encoding="utf8") as f:
    sh = f.read()

sh = sh.split(';')
dt = {}

for i in sh[:-1]:
    tp = i.split("=")
    try: 
        dt.update({tp[0] : tp[1]})
        # dt.update({tp[0] : tp[1].split("'")[1]})
    except: 
        pass

ec = sh[-1]
dr = ec.split('$')

with open('HostOnion.sh', 'w') as f:
    for i in dr:
        try: 
            print(dt[i], end='')
            f.write(dt[i])
        except: 
            pass

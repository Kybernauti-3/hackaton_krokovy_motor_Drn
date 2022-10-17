import utime as time
import machine

piny = [
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(4, machine.Pin.OUT),
    machine.Pin(5, machine.Pin.OUT),
]

otocka = [
    [0,1,1,1],
    [1,1,1,0],
    [1,1,0,1],
    [1,0,1,1]
    ]

while True:
    for krucek in otocka:
        for i in range(len(piny)):
            piny[i].value(krucek[i])
            time.sleep(0.01)





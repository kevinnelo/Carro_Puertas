
from time import sleep, sleep_ms
from machine import Pin as pin

puerta1 = pin(5, pin.IN, pin.PULL_UP)
puerta2 = pin(18, pin.IN, pin.PULL_UP)
puerta3= pin(19, pin.IN, pin.PULL_UP)
puerta4 = pin(21, pin.IN, pin.PULL_UP)

led = pin(22, pin.OUT)

while True:
    puerta_abierta = puerta1.value() or puerta2.value() or puerta3.value() or puerta4.value()

    led.value(puerta_abierta)
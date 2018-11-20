from time import sleep
from sense_hat import SenseHat
from wia import Wia


while(1):
    sense = SenseHat()
    temp=round(sense.get_temperature(),2)
    pres=round(sense.get_pressure(),2)
    humi=round(sense.get_humidity(),2)

    wia = Wia()
    wia.access_token = "d_sk_nDwown4c34Urw2MEwnmC9e9Q"
    
    wia.Event.publish(name="temperature", data=temp)
    wia.Event.publish(name="pressure", data=pres)
    wia.Event.publish(name="humidity", data=humi)
    sleep(15)
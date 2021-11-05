import paho.mqtt.client as paho
import time
import json
from threading import *

class App1(Thread):
    
    def run(self,topic):
        def on_publish(client, userdata, mid):
            print("msg.id: "+str(mid))

        data = {
            "user": "puntaric",
            "id": "XY123",
            "test_id": "TID123",
            "test_status": "OK",
            "finished": 0
        }

        data_json = json.dumps(data)

        host_ip="10.30.10.52"
        this_client_id = "Publisher-1"


        client = paho.Client(client_id=this_client_id, userdata=None, protocol=paho.MQTTv31)
        client.on_publish = on_publish
        client.will_set("my/pub_lastwill", this_client_id+ " Gone Offline",qos=1,retain=False)

        client.connect(host=host_ip, port=1883)
        client.loop_start()

        for i in range(49):   
            (rc, mid) = client.publish(topic, str(i), qos=1)
            time.sleep(0.5)

        (rc, mid) = client.publish(topic, str('x'), qos=1)
        time.sleep(5)
        #data["finished"]=1
        #data_json = json.dumps(data)


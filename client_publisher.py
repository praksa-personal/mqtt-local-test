import paho.mqtt.client as paho


def on_publish(client, userdata, mid):
    #print("msg.id: "+str(mid))
    ()
 
host_ip = "192.168.0.29"
this_client_id = "Publisher-Marko"


client = paho.Client(client_id=this_client_id, userdata=None, protocol=paho.MQTTv31)
client.on_publish = on_publish
client.will_set("my/lastwill", this_client_id+ " Gone Offline",qos=1,retain=False)

client.connect(host=host_ip, port=1883)
client.loop_start()

print("Enter topic name you want to publish to:")
topic = input()

while True:
    print("Enter message:")
    msg = input()
    (rc, mid) = client.publish(topic, str("From " + this_client_id + ": " + msg), qos=1)



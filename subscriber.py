import paho.mqtt.client as paho


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

host_ip = "10.30.10.52"
this_client_id = "Subscriber-Marko"

client = paho.Client(client_id=this_client_id, clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.will_set("my/lastwill", this_client_id+ " Gone Offline",qos=1,retain=False)

client.connect(host=host_ip, port=1883)

client.loop_start()

while True:
    print("Enter topic you want to subscribe to:")
    topic = input()
    client.subscribe(topic, qos=1)



import paho.mqtt.client as paho


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    if(msg.topic == "my/topic_1"):
        global msg_count_1
        msg_count_1 += 1
        #data = json.loads(msg.payload)
        if(msg.payload == b'x'):
            #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
            print("Test zavrsen, primljeno poruka na my/topic_1: ",msg_count_1)
            client.unsubscribe("my/topic_1")

    if(msg.topic == "my/topic_2"):
        global msg_count_2
        msg_count_2 += 1
        #data = json.loads(msg.payload)
        if(msg.payload == b'x'):
            #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
            print("Test zavrsen, primljeno poruka na my/topic_2: ",msg_count_2)
            client.unsubscribe("my/topic_2")

    
    if(msg.topic == "my/topic_3"):
        global msg_count_3
        msg_count_3 += 1
        #data = json.loads(msg.payload)
        if(msg.payload == b'x'):
            #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
            print("Test zavrsen, primljeno poruka na my/topic_3: ",msg_count_3)
            client.unsubscribe("my/topic_3")

host_ip="10.30.10.52"
this_client_id = "Subscriber-1"
msg_count_1 = 0
msg_count_2 = 0
msg_count_3 = 0

client = paho.Client(client_id=this_client_id, clean_session=False, userdata=None, protocol=paho.MQTTv31)
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(host=host_ip, port=1883)
client.subscribe("my/topic_1", qos=1)
client.subscribe("my/topic_2", qos=1)
client.subscribe("my/topic_3", qos=1)

client.loop_forever()



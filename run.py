from threading import *
from publisher import App1

app1 = App1()

t1 = Thread(target=app1.run,args=("my/topic_1",))
t1.start()

t2 = Thread(target=app1.run,args=("my/topic_2",))
t2.start()

t3 = Thread(target=app1.run,args=("my/topic_3",))
t3.start()
import time
from event import Event, EventType, EventBus


def func1(event):
    print(event.type, event.data)

def func2(event):
    print("lolo")

event_bus = EventBus()
event_bus.register(func1, EventType.TEST_EVENT)
event_bus.register(func2, "test")


while True:
    time.sleep(2)
    event_bus.emit(Event("test", {"test": 2}))

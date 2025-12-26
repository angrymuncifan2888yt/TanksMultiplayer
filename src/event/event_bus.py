class EventBus:
    def __init__(self):
        self.listeners = {}

    def register(self, handler, event_type):
        if event_type not in self.listeners:
            self.listeners[event_type] = []

        self.listeners[event_type].append(handler)

    def emit(self, event):
        for handler in self.listeners.get(event.type, []):
            handler(event)

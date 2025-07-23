import threading
from datetime import datetime

class URLStore:
    def __init__(self):
        self.store = {}
        self.lock = threading.Lock()

    def add(self, short_code, original_url):
        with self.lock:
            self.store[short_code] = {
                "url": original_url,
                "created_at": datetime.utcnow(),
                "clicks": 0
            }

    def get(self, short_code):
        return self.store.get(short_code)

    def increment_click(self, short_code):
        with self.lock:
            if short_code in self.store:
                self.store[short_code]["clicks"] += 1

    def stats(self, short_code):
        return self.store.get(short_code)

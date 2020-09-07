import time
class Messenger:
    db = []
    requested_count = 0
    def send_msg(self, name, text):
        timestamp = time.asctime()
        self.db.append({'name': name, 'text': text, 'timestamp': timestamp})

    def get_msgs(self):
        return self.db

    def get_new_msgs(self):
        new_msgs = self.db[self.requested_count:]
        self.requested_count += len(new_msgs)
        return new_msgs


msg = Messenger()
msg.send_msg('aaa', 'text')
msg.send_msg('aabbba', 'text')
print(msg.get_msgs())
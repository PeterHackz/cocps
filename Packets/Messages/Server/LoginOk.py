import time

from Utils.Writer import Writer


class LoginOk(Writer):
    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(0)
        self.writeInt(1)
        self.writeInt(0)
        self.writeInt(1)
        self.writeString("a77bad4dc5241ccb44d5a541376396208f92af8") #token

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString("dev") #env

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeString()       
        print("[DEBUG] Message LoginOk has been sent.")
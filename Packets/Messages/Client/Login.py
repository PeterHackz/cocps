# -*- coding: utf-8 -*-

from Utils.Reader import ByteStream
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Logic.Player import Player


class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device
    def decode(self):
        pass
    def process(self):
        LoginOk(self.client, self.player).Send()
        OwnHomeData(self.client, self.player).Send()

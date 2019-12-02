class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def vol_up(self):
        if self.volume<10:
            self.volume +=1
    def vol_down(self):
        if self.volume>0:
            self.volume -=1
    def set_channels(self,channels_list):
        self.channels = channels_list
    def show_channels(self):
        print('LISTA KANAŁÓW TV \n1. TVP1\n2. TVP2\n3. Polsat\n4. TVN\n5. Filmbox')
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            if self.channel_no-1>=len(self.channels):
                print('Telewizor jest załączony, ','kanał ',self.channel_no, ', Głośność: ',self.volume)
            else:
                print('Telewizor jest załączony, ','kanał ',self.channel_no, '(',self.channels[self.channel_no -1],'), Głośność: ',self.volume)
        else:
            print('Telewizor jest wyłączony')
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
tv1 = TV()
tv1.on()
tv1.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','CC','Fox'])
tv1.show_status()
tv1.vol_up()
tv1.vol_up()
tv1.show_status()
tv1.vol_down()
tv1.vol_down()
tv1.vol_down()
tv1.vol_down()
tv1.show_status()
tv1.off()

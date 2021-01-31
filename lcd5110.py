# PCD8544 (Nokia 5110) LCD sample for Raspberry Pi Pico
# Required library:
#   https://github.com/mcauser/micropython-pcd8544
# And this sample script is based on above repository.

# Connections:
#   [pcd8544:pico(physical pin)]
#   Gnd: Pico GND (38)
#   BL : Pico GP28(34)
#   Vcc: Pico 3V3 (36)
#   Clk: Pico GP6 ( 9)
#   Din: Pico GP7 (10)
#   DC : Pico GP4 ( 6)
#   CE : Pico GP5 ( 7)
#   RST: Pico GP8 (11)

import pcd8544_fb
from machine import Pin, SPI
import utime
import framebuf


class LCD5110:
    def __init__(self,spi=0,cs=5,dc=4,rst=8,bl=28):
        self.spi= SPI(spi)
        self.spi.init(baudrate=2000000,
                      polarity=0,
                      phase=0)
        self.cs = Pin(cs)
        self.dc = Pin(dc)
        self.rst = Pin(rst)
        self.bl = Pin(bl, Pin.OUT, value=1)
        self.lcd = pcd8544_fb.PCD8544_FB(self.spi,
                                         self.cs,
                                         self.dc,
                                         self.rst)

        self.buffer = bytearray((pcd8544_fb.HEIGHT // 8) * pcd8544_fb.WIDTH)
      
        self.framebuf = framebuf.FrameBuffer(self.buffer,
                                         pcd8544_fb.WIDTH,
                                         pcd8544_fb.HEIGHT,
                                         framebuf.MONO_VLSB)
        self.HEIGHT = pcd8544_fb.HEIGHT
        self.WIDTH  = pcd8544_fb.WIDTH
        self.clear()
    
    def clear(self):
        # clear
        self.framebuf.fill(0)
        self.update()

    def text(self,string,x,y,color,update=False):
        self.framebuf.text(string,x,y,color)
        if update:
            self.update()

    def fill_rect(self,x, y, w, h, c, update=False):
        self.framebuf.fill_rect(x,y,w,h,c)
        if update:
            self.update()
        

    def update(self):
        self.lcd.data(self.buffer)



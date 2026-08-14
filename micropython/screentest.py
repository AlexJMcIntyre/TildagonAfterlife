from machine import Pin, SPI
import gc9a01py as gc9a01
import vga1_bold_16x16

spi = SPI(
    1,
    baudrate=40_000_000,
    polarity=0,
    phase=0,
    sck=Pin(1),
    mosi=Pin(6),
)

tft = gc9a01.GC9A01(
    spi=spi,
    dc=Pin(3, Pin.OUT),
    cs=Pin(7, Pin.OUT),
    reset=Pin(8, Pin.OUT),
    rotation=2
)

tft.fill(gc9a01.BLACK)

tft.text(
    vga1_bold_16x16,
    "This screen",
    30,
    70,
    gc9a01.RED,
    gc9a01.BLACK,
)

tft.text(
    vga1_bold_16x16,
    "seems",
    40,
    110,
    gc9a01.GREEN,
    gc9a01.BLACK,
)

tft.text(
    vga1_bold_16x16,
    "to work!",
    30,
    150,
    gc9a01.BLUE,
    gc9a01.BLACK,
)
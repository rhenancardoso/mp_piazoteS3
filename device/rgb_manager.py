from neopixel import NeoPixel
from utils import RgbIndicator

STEP = 0.1
MAX_BRIGHT = 1


class LightCycle:
    FIXED = 0
    UPNDOWN = 1
    UPONLY = 2


class Fade:
    BRIGHT = 0
    DARK = 1


class RgbManager:
    def __init__(self, neopixel: NeoPixel, light_cycle: LightCycle) -> None:
        self.neopixel = neopixel
        self.brightness = 1
        self.cycle = light_cycle
        self.current_cycle = Fade.BRIGHT if light_cycle == LightCycle.UPNDOWN else None

    def set_rgb_led(self, Color: RgbIndicator):
        self._update_brightness()
        self.neopixel[0] = tuple(int(value * self.brightness) for value in Color)
        self.neopixel.write()

    def _update_brightness(self):
        if self.cycle == LightCycle.FIXED:
            self.brightness = MAX_BRIGHT

        elif self.cycle == LightCycle.UPONLY:
            self.brightness = (self.brightness + STEP) if self.brightness >= 1 else STEP

        elif self.cycle == LightCycle.UPNDOWN and self.current_cycle == Fade.BRIGHT:
            self.brightness += STEP
            if self.brightness >= MAX_BRIGHT:
                self.current_cycle = Fade.DARK
                self.brightness = MAX_BRIGHT

        elif self.cycle == LightCycle.UPNDOWN and self.current_cycle == Fade.DARK:
            self.brightness -= STEP
            if self.brightness <= STEP:
                self.current_cycle = Fade.BRIGHT
                self.brightness = STEP

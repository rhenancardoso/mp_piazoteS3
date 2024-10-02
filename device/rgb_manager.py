from neopixel import NeoPixel
from utils import RgbIndicator

STEP = 0.02
TICK = 0.3
MAX_BRIGHT = 1


class LightPattern:
    FIXED = 0
    UPNDOWN = 1
    UPONLY = 2
    BLINK = 3


class Cycle:
    BRIGHT = 0
    DARK = 1


class RgbManager:
    def __init__(self, neopixel: NeoPixel, light_cycle: LightPattern) -> None:
        self.neopixel = neopixel
        self.brightness = 1
        self.tick = 1
        self.cycle = light_cycle
        self.current_cycle = (
            Cycle.BRIGHT if light_cycle == LightPattern.UPNDOWN else None
        )

    def set_cycle_style(self, cycle_type: LightPattern):
        """Set the RGB cycle."""
        if self.cycle != cycle_type:
            self.cycle = cycle_type
            self.current_cycle = Cycle.BRIGHT

    def set_rgb_led(self, Color: RgbIndicator):
        """Set RGB color"""
        self._update_brightness()
        self.neopixel[0] = tuple(int(value * self.brightness) for value in Color)
        self.neopixel.write()

    def _update_brightness(self):
        if self.cycle == LightPattern.FIXED:
            self.brightness = MAX_BRIGHT

        elif self.cycle == LightPattern.UPONLY:
            self.brightness += STEP
            if self.brightness >= 1:
                self.brightness = STEP

        elif self.cycle == LightPattern.UPNDOWN:
            self._update_upndown_cycle()

        elif self.cycle == LightPattern.BLINK:
            self._update_blink_cycle()

    def _update_blink_cycle(self):
        if self.current_cycle == Cycle.BRIGHT:
            self._increase_tick()
        elif self.current_cycle == Cycle.DARK:
            self._decrease_tick()

    def _update_upndown_cycle(self):
        if self.current_cycle == Cycle.BRIGHT:
            self._increase_brightness()
        elif self.current_cycle == Cycle.DARK:
            self._decrease_brightness()

    def _increase_brightness(self):
        self.brightness += STEP * 2
        if self.brightness >= MAX_BRIGHT:
            self.current_cycle = Cycle.DARK
            self.brightness = MAX_BRIGHT

    def _decrease_brightness(self):
        self.brightness -= STEP * 2
        if self.brightness <= STEP * 2:
            self.current_cycle = Cycle.BRIGHT
            self.brightness = STEP * 2

    def _increase_tick(self):
        self.tick += TICK
        if self.tick >= MAX_BRIGHT:
            self.current_cycle = Cycle.DARK
            self.tick = MAX_BRIGHT
            self.brightness = 0

    def _decrease_tick(self):
        self.tick -= TICK
        if self.tick <= TICK:
            self.current_cycle = Cycle.BRIGHT
            self.tick = TICK
            self.brightness = MAX_BRIGHT

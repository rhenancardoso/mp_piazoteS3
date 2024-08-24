import json


class config:
    """Class to retrieve the config data"""

    ap_ssid: str
    ap_password: str

    def __init__(self) -> None:
        self._loadConfigJson()

    def _loadConfigJson(self):
        """Extract data from JSON file"""
        with open("config.json") as config_f:
            print("Loading JSON object")
            config_data = json.load(config_f)
            self.ap_ssid = config_data["AP_SSID"]
            self.ap_password = config_data["AP_PASS"]
            print("Configuration object loaded")

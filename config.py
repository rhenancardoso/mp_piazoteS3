import json


def sort_word_keys(dict: dict) -> list:
    """Sort the keys of a dictionary."""
    keys = list(dict.keys())
    keys.sort()
    return keys


class config:
    """Class to retrieve the config data"""

    def __init__(self) -> None:
        self._loadConfigJson()

    def _loadConfigJson(self):
        """Extract data from JSON file"""
        with open("config.json") as config_f:
            print("Loading JSON object")
            config_data = json.load(config_f)
            self.ap_ssid = config_data["AP_SSID"]
            self.ap_password = config_data["AP_PASS"]
            self.ap_words = [
                config_data["AP_WORDS"][key]
                for key in sort_word_keys(config_data["AP_WORDS"])
            ]
            print("Configuration object loaded")

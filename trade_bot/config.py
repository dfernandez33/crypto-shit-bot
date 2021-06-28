# Config consts
import configparser
import os

CFG_FL_NAME = "user.cfg"
USER_CFG_SECTION = "binance_user_config"


class Config:  # pylint: disable=too-few-public-methods,too-many-instance-attributes
    def __init__(self):
        # Init config
        config = configparser.ConfigParser()
        config["DEFAULT"] = {
            "tld": "com",
            "strategy": "default",
        }

        if not os.path.exists(CFG_FL_NAME):
            print("No configuration file (user.cfg) found! See README. Assuming default config...")
            config[USER_CFG_SECTION] = {}
        else:
            config.read(CFG_FL_NAME)

        # Get config for binance
        self.BINANCE_API_KEY = config.get(USER_CFG_SECTION, "api_key")
        self.BINANCE_API_SECRET_KEY = config.get(USER_CFG_SECTION, "api_secret_key")
        self.BINANCE_TLD = config.get(USER_CFG_SECTION, "tld")

        # Get supported coin list from supported_coin_list file
        if os.path.exists("supported_coin_list"):
            supported_coin_list = []
            with open("supported_coin_list") as rfh:
                for line in rfh:
                    line = line.strip()
                    if not line or line.startswith("#") or line in supported_coin_list:
                        continue
                    supported_coin_list.append(line)

            self.SUPPORTED_COIN_LIST = supported_coin_list
        else:
            raise Exception("No 'supported_coin_list' file found, please create and try again.")

        self.STRATEGY = config.get(USER_CFG_SECTION, "strategy")

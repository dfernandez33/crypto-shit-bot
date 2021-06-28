from trade_bot.config import Config
from binance.client import Client


if __name__ == '__main__':
    # Place call to main execution loop when ready
    config = Config()
    client = Client(config.BINANCE_API_KEY, config.BINANCE_API_SECRET_KEY, tld=config.BINANCE_TLD)

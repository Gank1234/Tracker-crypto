from scr.http_client import CMC_HTTPClient
from scr.config import settings

cmc_client = CMC_HTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)
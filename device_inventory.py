from api_client import api_get
from config import DEVICE_ENDPOINT


def get_device_inventory(token):
    devices = api_get(DEVICE_ENDPOINT, token)
    return devices
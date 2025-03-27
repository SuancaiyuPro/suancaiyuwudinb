import requests
import json
import time
from typing import Optional, Dict, Any

class SuancaiyuAPIClient:
    """
    A lightweight and robust API client for handling common HTTP requests.
    """
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        return self.request("POST", endpoint, json=data)

def format_timestamp(ts: float = None) -> str:
    """Formats a unix timestamp into a human-readable string."""
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts or time.time()))

if __name__ == "__main__":
    # Example usage
    client = SuancaiyuAPIClient("https://api.github.com")
    print(f"Current Time: {format_timestamp()}")
    # print(client.get("zen"))

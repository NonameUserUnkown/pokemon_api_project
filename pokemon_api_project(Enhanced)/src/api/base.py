import requests
from typing import Dict, Any, Optional
from utils.validators import validate_response


class BaseAPIClient:
    """Base class for API clients"""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[
        str, Any]:
        """Make HTTP request to the API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                timeout=self.timeout,
                **kwargs
            )
            return validate_response(response)

        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        return self._make_request('GET', endpoint, **kwargs)
from typing import Dict, Any
import requests

def validate_response(response: requests.Response) -> Dict[str, Any]:
    """Validate and process API response"""
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 404:
            return {"error": "Resource not found"}
        return {"error": f"HTTP error {status_code}"}
    except ValueError:
        return {"error": "Invalid JSON response"}
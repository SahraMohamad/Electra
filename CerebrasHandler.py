import requests
import os

class CerebrasHandler:
    '''
    Handler for interacting with the Cerebras API
    '''
    CEREBRAS_URL = 'https://api.cerebras.ai/v1/chat/completions'
    def __init__(self, model_name, api_keys):
        """
        """
        self.model_name = model_name
        self.api_keys = api_keys
        self.current_key_index = 0

    def _get_next_api_key(self):
        """Cycle to the next API key in the list."""
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        print("_get_next_api_key called")
        return self.api_keys[self.current_key_index]

    def _make_api_call(self, messages, params=None):
        '''
        Internal function to make a chat completion call to Cerebras
        '''
        current_key = self.api_keys[self.current_key_index]
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {current_key}"
        }
        data = {
            "model": self.model_name,
            "stream": False,
            "messages": messages,
            "temperature": 0.1,
            "max_tokens": -1
        }
        
        # Try to make a request to the Cerebras chat completion API
        try:
            response = requests.post(self.CEREBRAS_URL, headers=headers, json=data)
            if response.status_code == 429:  # HTTP 429 Too Many Requests
                print(f"API key {current_key} hit limit.")
                return None 
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API call: {e}")
            return None

    def call_api(self, messages, params=None):
        '''
        Public function to make a call to Cerebras API.
        This function will rotate to the next key if the currently active
        api key has reached its limit.
        '''
        attempts = 0
        while attempts < len(self.api_keys):
            result = self._make_api_call(messages=messages, params=params)
            if result is not None:
                return result
            self._get_next_api_key()
            attempts += 1
        print("NO API CALLS MADE")
        return None

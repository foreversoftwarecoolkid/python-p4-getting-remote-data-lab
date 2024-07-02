import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url
    
    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Ensure we raise an exception for bad responses
        return response.content  # Use .content to get the raw bytes of the response body
    
    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Example usage
if __name__ == "__main__":
    get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
    print(get_requester.load_json())

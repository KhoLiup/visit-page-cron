import requests

class SiteVisitor:
    def __init__(self, url):
        self.url = url

    def visit(self):
        try:
            response = requests.get(self.url)
            self._log_response(response)
        except requests.exceptions.RequestException as e:
            self._log_error(e)

    def _log_response(self, response):
        print(f"Visited {self.url}")
        print(f"Status Code: {response.status_code}")
        if response.ok:
            print(f"Response Content: {response.text[:100]}...")  # İlk 100 simvolu göstərir
        else:
            print("Failed to retrieve the content.")

    def _log_error(self, error):
        print(f"Error visiting site: {error}")


if __name__ == "__main__":
    url = "https://wp.pavilion.az/send_reminder.php"
    visitor = SiteVisitor(url)
    visitor.visit()

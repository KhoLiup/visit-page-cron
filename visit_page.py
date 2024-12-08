import requests

def visit_site():
    url = "http://wp.pavilion.az/send_reminder.php"
    try:
        response = requests.get(url)
        print(f"Visited {url} - Status Code: {response.status_code}")
        print(f"Response Content: {response.text[:100]}...")  # İlk 100 simvolu göstərir
    except Exception as e:
        print(f"Error visiting site: {e}")

if __name__ == "__main__":
    visit_site()

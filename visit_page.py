import requests

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"
    cookies = {
        "sc_is_visitor_unique": "rx9692532.1732373051.ACBEB28A2EBA485A955BE12AD038E0AC.2.2.2.2.2.2.2.2.1",
        "PHPSESSID": "66c311fe424a87b9dd83871097adaf3e",
        "__test": "1759c0b2cc931d85f96464b9dced7e0c"
    }

    try:
        response = requests.get(url, cookies=cookies)
        print(f"Visited {url} - Status Code: {response.status_code}")
        print(f"Response: {response.text[:100]}...")
    except Exception as e:
        print(f"Error visiting page: {e}")

if __name__ == "__main__":
    visit_page()

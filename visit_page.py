import requests
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək səhifənin URL-si
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # GET sorğusu göndərilir, User-Agent əlavə edilib
        print(f"Visiting {url}...")
        response = requests.get(url, headers=headers, timeout=10, verify=False)

        # Status kodunu yoxlayın və nəticəni log edin
        print(f"Visited {url} - Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Page visited successfully!")
            print(f"Response Content (first 100 characters): {response.text[:100]}...")

            # 10 saniyə gözləyin
            print("Staying on the page for 10 seconds...")
            time.sleep(10)
            print("Finished waiting for 10 seconds.")
        else:
            print(f"Failed to visit the page. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error visiting page: {e}")


if __name__ == "__main__":
    visit_page()

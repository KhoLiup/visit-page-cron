import requests
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək səhifənin URL-si

    try:
        # SSL doğrulamasını keçmək üçün `verify=False` əlavə edilib
        response = requests.get(url, timeout=10, verify=False)

        # Status kodunu və nəticəni çap edin
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

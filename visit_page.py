import requests
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək səhifənin URL-si
    try:
        print(f"Visiting {url}...")
        response = requests.get(url)  # GET sorğusu göndərilir
        print(f"Visited {url} - Status Code: {response.status_code}")  # Status kodunu çap edir
        
        if response.status_code == 200:
            print("Staying on the page for 10 seconds...")
            time.sleep(10)  # 10 saniyə gözləyir
            print("Done staying on the page.")
        else:
            print(f"Failed to visit the page. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error visiting page: {e}")

if __name__ == "__main__":
    visit_page()

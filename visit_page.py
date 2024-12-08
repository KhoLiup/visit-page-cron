from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək səhifənin URL-si

    # Chrome parametrləri
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Görünməz rejim
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        # Brauzeri başlat
        driver = webdriver.Chrome(options=options)
        print(f"Opening {url}...")
        
        # URL-i ziyarət et
        driver.get(url)
        print(f"Visited {url}")

        # 10 saniyə gözlə
        print("Staying on the page for 10 seconds...")
        time.sleep(10)

        # İş tamamlandı
        print("Finished waiting for 10 seconds.")
        driver.quit()  # Brauzeri bağla
    except Exception as e:
        print(f"Error visiting page: {e}")


if __name__ == "__main__":
    visit_page()

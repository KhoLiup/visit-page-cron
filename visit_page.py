from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"

    # Chrome parametrləri
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    try:
        driver = webdriver.Chrome(options=options)
        print(f"Opening {url}...")
        
        driver.get(url)
        print(f"Visited {url}")

        # 10 saniyə gözlə
        print("Staying on the page for 10 seconds...")
        time.sleep(10)

        # İş tamamlandı
        print("Finished waiting for 10 seconds.")
        driver.quit()
    except Exception as e:
        print(f"Error visiting page: {e}")


if __name__ == "__main__":
    visit_page()

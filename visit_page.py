from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def visit_page():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək səhifənin URL-si

    # Chrome parametrləri
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Görünən rejim (headless-dən qaçmaq üçün)
    # Headless olmadan bir brauzer pəncərəsi açır
    options.add_argument("--start-maximized")

    # Yavaş yüklənmələr üçün random gecikmələr əlavə edin
    def random_delay():
        time.sleep(random.uniform(2, 5))

    try:
        # ChromeDriver xidmətini başladın
        driver = webdriver.Chrome(options=options)
        print(f"Opening {url}...")

        # Səhifəni ziyarət edin
        driver.get(url)
        print(f"Visited {url}")

        # Random gecikmə
        random_delay()

        # Dinamik məzmunların yüklənməsini gözləyin
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Page loaded successfully.")
        except Exception as e:
            print("Dynamic content load timeout:", e)

        # Gözləmə (10 saniyə qalma)
        print("Staying on the page for 10 seconds...")
        time.sleep(10)

        # İş tamamlandı
        print("Finished waiting on the page.")
        driver.quit()  # Brauzeri bağlayın
    except Exception as e:
        print(f"Error visiting page: {e}")


if __name__ == "__main__":
    visit_page()

import requests

def visit_site():
    # Ziyarət edəcəyiniz saytın URL-si
    url = "http://wp.pavilion.az/send_reminder.php"

    try:
        # Sayta GET sorğusu göndərilir
        response = requests.get(url)

        # Cavab status kodunu və məzmununu yoxlayırıq
        print(f"Visited {url} - Status Code: {response.status_code}")
        print(f"Response Content: {response.text[:100]}...")  # İlk 100 simvolu göstərir
    except Exception as e:
        # Əgər bir xəta baş verərsə, xətanı çap edir
        print(f"Error visiting site: {e}")

# Saytı ziyarət edin
visit_site()

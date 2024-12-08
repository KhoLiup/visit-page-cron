import requests

# Saytı ziyarət edən funksiya
def visit_site():
    url = "http://wp.pavilion.az/send_reminder.php"  # Ziyarət ediləcək saytın URL-si
    response = requests.get(url)  # Sayta GET sorğusu göndər

# Saytı ziyarət et
visit_site()

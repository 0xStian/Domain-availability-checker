import whois    # pip install python-whois
from random import choice

available_domains = "available_domains.txt"
show_unavailable_domains = True
letters = 4

def get_random_string(size=letters, chars="1234567890qwertyuioplkjhgfdsazxcvbnm"):
    return ''.join(choice(chars) for _ in range(size))


def send_request(domain):
    try:
        get_info = whois.whois(domain)
        return False
    except:
        return True


while True:
    current_domain = str(get_random_string() + ".com")

    if send_request(current_domain) is True:
        print(f"X | {current_domain} | is available")
        available = open(available_domains, "a")
        available.write(f"{str(current_domain)}\n")
        available.close()

    elif show_unavailable_domains is True:
        print(f"  | {current_domain} | is unavailable")

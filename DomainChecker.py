import whois    # pip install python-whois
from random import choice

available_domains = "available_domains.txt"                 # what file to save available domains to
show_unavailable_domains = True                             # print unavailable domains to console
letters = 4                                                 # how many letters/numbers in generated domain
TDL = ".com"                                                # what TDL to use
letters_to_include = "1234567890qwertyuioplkjhgfdsazxcvbnm" # what letters and numbers will be included in the randomly generated domain

# generate the random domain
def get_random_string(size=letters, chars=letters_to_include):
    return ''.join(choice(chars) for _ in range(size))

# check if domain is available
def send_request(domain):
    try:
        get_info = whois.whois(domain)
        return False
    except:
        return True


while True:
    current_domain = str(get_random_string() + TDL)

    if send_request(current_domain) is True:
        print(f"X | {current_domain} | is available")
        available = open(available_domains, "a")
        available.write(f"{str(current_domain)}\n")
        available.close()

    elif show_unavailable_domains is True:
        print(f"  | {current_domain} | is unavailable")

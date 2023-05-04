import requests

target_input = "google.com"

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()

        try:
            url = "http://" + word + "." + target_input
            response = requests.get(url)
            print(response.status_code)
            if response:
                print("Found subdomain ---> " + url)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

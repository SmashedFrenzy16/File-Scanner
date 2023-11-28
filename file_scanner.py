import cloudmersive_virus_api_client as virus_scan
from cloudmersive_virus_api_client.rest import ApiException
import cloudmersive_security_api_client as security_scan
from cloudmersive_security_api_client.rest import ApiException
from pprint import pprint

api_key = input("Enter in your API key: ")

def main():
    path = input("Enter in your file path: ")

    print("Which scan would you like to perform on the file?: ")
    print("1. Virus Scan")
    print("2. Security Scan")

    choice = int(input("Enter in your choice (1 or 2): "))

    if choice == 1:

        config = virus_scan.Configuration()

        config.api_key["Apikey"] = api_key

        instance = virus_scan.ScanApi(virus_scan.ApiClient(config))

        try:

            response = instance.scan_file(path)

            pprint(f"Virus Scan Results: {response}")

        except ApiException as a:

            print(a)



    elif choice == 2:

        config = virus_scan.Configuration()

        config.api_key["Apikey"] = api_key

        instance = security_scan.ContentThreatDetectionApi(security_scan.ApiClient(config))

        try:

            response = instance.content_threat_detection_automatic_threat_detection_string(path)

            pprint(f"Security Scan Results: {response}")

        except ApiException as a:

            print(a)

    else:
        print("Invalid choice. Please choose again.")

while True:

    main()

    scan_again = input("Do you want to scan another file (y/n)?: ")

    if scan_again == "n" or scan_again == "N":

        break




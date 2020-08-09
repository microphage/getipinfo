import argparse
import json
from urllib.request import urlopen

def get_ip():
    """
    Positional argument for IPv4 address
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("ip_address")
    return parser.parse_args()


def main():
    """
    Get Geolocation information from ipvigilante.com and display.
    """
    ip_obj = get_ip()
    url = ("http://ipvigilante.com/" + ip_obj.ip_address + "/full")
    response = urlopen(url)
    data_json = response.read().decode("utf-8")
    geoloc = json.loads(data_json)

    # print(geoloc)
    print("ipv4: ", geoloc['data']['ipv4'])
    print("hostname: ", geoloc['data']['hostname'])
    print("continent_code: ", geoloc['data']['continent_code'])
    print("continent_name: ", geoloc['data']['continent_name'])
    print("country_iso_code: ", geoloc['data']['country_iso_code'])
    print("country_name: ", geoloc['data']['country_name'])
    print("subdivision_1_iso_code: ", geoloc['data']['subdivision_1_iso_code'])
    print("subdivision_1_name: ", geoloc['data']['subdivision_1_name'])
    print("subdivision_2_iso_code: ", geoloc['data']['subdivision_2_iso_code'])
    print("subdivision_2_name: ", geoloc['data']['subdivision_2_name'])
    print("city_name: ", geoloc['data']['city_name'])
    print("metro_code: ", geoloc['data']['metro_code'])
    print("time_zone: ", geoloc['data']['time_zone'])
    print("postal_code: ", geoloc['data']['postal_code'])
    print("latitude: ", geoloc['data']['latitude'])
    print("longitude: ", geoloc['data']['longitude'])
    print("accuracy_radius: ", geoloc['data']['accuracy_radius'])


if __name__ == "__main__":
    main()

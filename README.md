# getipinfo

Get IP address and geolocation via command line.

## Usage:

* getipinfo.sh - gets your current external IP address from 2 sites
  ipinfo.io/ip and ifconfig.me and queries ipvigilante.com for geolocation.

```
$ ./getipinfo.sh

via ipinfo.io/ip
"8.8.8.8"
"California"
"Mountain View"
"United States"
via ifconfig.me
"8.8.8.8"
"California"
"Mountain View"
"United States"
```

* getipinfo.py - needs IP address as argument to display all geolocation
  information from ipvigilante.com.

```
$ python3 getipinfo.py 8.8.8.8

ipv4:  8.8.8.8
hostname:  dns.google
continent_code:  NA
continent_name:  North America
country_iso_code:  US
country_name:  United States
subdivision_1_iso_code:  CA
subdivision_1_name:  California
subdivision_2_iso_code:  None
subdivision_2_name:  None
city_name:  Mountain View
metro_code:  807
time_zone:  America/Los_Angeles
postal_code:  94035
latitude:  37.38600
longitude:  -122.08380
accuracy_radius:  1000
```

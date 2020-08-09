#! /usr/bin/env zsh
echo "via ipinfo.io/ip"
ip_address1=`curl -s https://ipinfo.io/ip`
geoloc_data=`curl -s https://ipvigilante.com/${ip_address1}`
echo ${geoloc_data} | jq '.data.ipv4, .data.subdivision_1_name, .data.city_name, .data.country_name'

echo "via ifconfig.me"
ip_address2=`curl -s https://ifconfig.me`
geoloc_data2=`curl -s https://ipvigilante.com/${ip_address2}`
echo ${geoloc_data} | jq '.data.ipv4, .data.subdivision_1_name, .data.city_name, .data.country_name'

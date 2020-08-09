#! /usr/bin/env zsh
ip_address=`curl -s https://ipinfo.io/ip`
geoloc_data=`curl -s https://ipvigilante.com/${ip_address}`
echo ${geoloc_data} | jq '.data.ipv4, .data.subdivision_1_name, .data.city_name, .data.country_name'

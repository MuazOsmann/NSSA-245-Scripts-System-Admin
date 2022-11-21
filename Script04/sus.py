from geoip import geolite2
import re

match = geolite2.lookup('218.25.208.92')
print(match.country)
match2 = geolite2.lookup('8.19.245.2')
print(match2.country)
match3 = geolite2.lookup('183.3.202.111')
print(match3.country)
match4 = geolite2.lookup('195.154.49.74')
print(match4.country)
match5 = geolite2.lookup('159.122.220.20')
print(match5.country)
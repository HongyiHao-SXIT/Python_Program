import datetime

start_date = datetime.datetime(2009, 9, 25)
speed_mph = 38241
miles_to_km = 1.609344
miles_to_au = 92955887.6
speed_of_light = 299792458 / 1609.344

input_date_str = input("Please enter a date after September 25, 2009 (format: YYYYMMDD): ")
input_date = datetime.datetime.strptime(input_date_str, '%Y%m%d')

time_difference = (input_date - start_date).total_seconds() / 3600
distance_miles = speed_mph * time_difference + 16637000000
distance_km = distance_miles * miles_to_km
distance_au = distance_miles / miles_to_au
round_trip_time = (2 * distance_miles / speed_of_light) / 3600

print(f"Distance in miles: {distance_miles} miles")
print(f"Distance in kilometers: {distance_km} kilometers")
print(f"Distance in astronomical units: {distance_au} AU")
print(f"Round - trip time for radio communication: {round_trip_time} hours")
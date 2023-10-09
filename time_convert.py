from datetime import datetime, timedelta
import sys

if len(sys.argv) < 2:
    print("Please provide a UTC timestamp as an argument.")
    print('''Example : python time.py "2023-05-01 10:10:00"''')
    sys.exit(1)

utc_timestamp_str = sys.argv[1]
utc_datetime = datetime.strptime(utc_timestamp_str, "%Y-%m-%d %H:%M:%S")
gmt_offset = timedelta(hours=5, minutes=30)
ist_datetime = utc_datetime + gmt_offset

# Format the GMT+5.30 datetime as a string with AM/PM
ist_timestamp_str = ist_datetime.strftime("%Y-%m-%d %I:%M:%S %p")

# Fomat the GMT+5.30 without AM/PM
ist_wi_timestamp_str = ist_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("UTC Timestamp:", utc_timestamp_str)
print("GMT+5.30 Timestamp without AM/PM:", ist_wi_timestamp_str)
print("GMT+5.30 Timestamp:", ist_timestamp_str)

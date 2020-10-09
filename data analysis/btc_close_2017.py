import json
# import requests

# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
# response = requests.get(json_url)
# content = response.content.decode()
# with open("./btc_close_2017_request.json", "w") as f:
#     f.write(content)

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))

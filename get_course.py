import requests
from datetime import date, datetime, timedelta
from json import dump
import sys



def datespan(start, end, delta=timedelta(days=1)):
    current = start
    while current < end:
        yield current
        current += delta


with open(sys.argv[1], 'w') as file:
    for dates in datespan(date(2021, 1, 1), date(2021,2,1),delta=timedelta(days=1)):
        day = str(dates).replace("-", "")
        res = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={0}&date={1}&json".format(sys.argv[2],day))
        dump(res.json(), file,
            sort_keys=False,
            ensure_ascii=False,
            separators=(',', ': '),
            indent=4)


with open(sys.argv[1],'r') as file:
    data = file.read()
    data = data.replace("][",",")

with open(sys.argv[1],'w') as file:
    file.write(data)


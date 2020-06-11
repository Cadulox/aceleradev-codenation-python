from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]

PERMANENT_FEE = 0.36
CALL_FEE = 0.09
START_FARE = 6
END_FARE = 22


def sorting_criteria(element):
    return element['total']


def classify_by_phone_number(records):
    sorted_list = list()
    for call in records:
        call['cost'] = PERMANENT_FEE

        call_start = datetime.fromtimestamp(call['start'])
        call_end = datetime.fromtimestamp(call['end'])
        if call_start.hour >= START_FARE and call_start.hour < END_FARE:
            call_time = call_end - call_start
            minutes = int(call_time.seconds / 60)
            call['cost'] += minutes * CALL_FEE

        found_source = False
        for item in range(len(sorted_list)):
            if sorted_list[item]['source'] == call['source']:
                found_source = True
                sorted_list[item]['total'] += call['cost']

        if not found_source:
            new_source = {'source': call['source'], 'total': call['cost']}
            sorted_list.append(new_source)

    for item in range(len(sorted_list)):
        sorted_list[item]['total'] = round(sorted_list[item]['total'], 2)

    sorted_list.sort(reverse=True, key=sorting_criteria)

    return sorted_list

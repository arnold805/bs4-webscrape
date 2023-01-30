import requests, csv
from bs4 import BeautifulSoup

url = requests.get('https://www.iihs.org/ratings/vehicle/Subaru/forester-4-door-suv/2020')

soup = BeautifulSoup(url.text, 'html.parser')

iihs = soup.find('div', attrs={'class': 'hero-body'})

file = open('iihs_test.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['vehicle',
            'top_safety_pick',
            'small_overlap_front_drivers_side',
            'small_overlap_front_passenger_side',
            'moderate_overlap_front',
            'side_original',
            'side_updated_test',
            'roof_strength',
            'head_restraints_and_seat',
            'headlights',
            'front_crash_prevtion_vehicle_to_vehicle',
            'front_crash_prevtion_vehicle_to_pedestrian_day',
            'front_crash_prevtion_vehicle_to_pedestrian_night',
            'seat_belt_reminders',
            'latch_ease_of_use',
            ]
writer.writerow(headers)

CATEGORIES = [
    'vehicle_name'
    'top_safety_pick',
    'Small overlap front: driver-side',
    'Small overlap front: passenger-side',
    'Moderate overlap front: original test',
    'Side: original test',
    'Side: updated test',
    'Roof strength',
    'Head restraints & seats',
    'Headlights (varies by trim/option)',
    'Front crash prevention: vehicle-to-vehicle',
    'Front crash prevention: vehicle-to-pedestrian (day)',
    'Front crash prevention: vehicle-to-pedestrian (night)',
    'Seat belt reminders',
    'LATCH ease of use'
]

def vehicle_name():
    return iihs.find('h1', attrs={'class': 'head'}).text
    
print(vehicle_name())

def top_safety_pick():
    tsp = iihs.find('span', attrs={'class': 'tsp'})
    tsp_plus = iihs.find('span', attrs={'class': 'tspPlus'})

    if (tsp):
        return tsp.text
    elif(tsp_plus):
        return tsp_plus.text
    else:
        return

print(top_safety_pick())

def latch():
    latch = iihs.find('div', attrs={'style': 'display: flex; justify-content: center; align-items: center;'})
    latch_plus = iihs.find('span', attrs={'class': 'gamp-plus'})

    if (latch):
        return latch.text.strip()
    elif(latch_plus):
        return latch_plus.text.strip()
    else:
        return

print(latch())


def extract_rows(table):
    return table.find_all('tr')

rating_tables = iihs.find_all('table', attrs={'class': 'rating-table'})
table_row_lists = map(extract_rows, rating_tables)
rating_rows = [item for sub_list in table_row_lists for item in sub_list]

rating_rows =  filter(lambda x: not x is None and x.find('a'), rating_rows)

for rating_row in rating_rows:
    try:
        category = rating_row.find('a').text
        print(category)
        rating_div = rating_row.find('div', attrs={'class': 'rating-icon-block'})
        # extract single rating
        if rating_div:
            # extract the aria label attribute value from the span elements
            rating_spans = rating_row.find_all('span')
            ratings = list(map(lambda x: x['aria-label'], rating_spans))
            print(ratings)
        
        else:
            standard_system_row = rating_row.find_next_sibling()
            ca_rating_div = standard_system_row.find('div').text.strip()
            print(ca_rating_div)

    except:
        print('Error occured: KeyError: aria-label')

    # if plus_span:
    #     # ratings = list(map(lambda x: x['aria-label'], rating_spans))
    #     print(plus_span)
    
        # rating = rating_div.find('div').text
        # print(rating_div)

    # Is the rating a ca-rating or a rating-icon-block?
    # choose strategy for getting value depending on type of rating

# for category in CATEGORIES:
#     print(category)

file = open('iihs_test.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(file)
header = ([vehicle_name(),
            top_safety_pick(),
            latch(),
            ])
writer.writerow(header)
file.close()
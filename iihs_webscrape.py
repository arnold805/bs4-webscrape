import requests, csv
from bs4 import BeautifulSoup

#  check for __iter__ magic method, therefore data is iterable
# print(dir(iihs_index))

url = requests.get('https://www.iihs.org/ratings/vehicle/volkswagen/golf-gti-4-door-hatchback/2022')

soup = BeautifulSoup(url.text, 'html.parser')
# iihs = BeautifulSoup(html_doc, 'html.parser')

iihs = soup.find_all('div', attrs={'class': 'hero-body'})

file = open('iihs_test.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['vehicle',
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
            'latch_ease_of_use'
            ]
writer.writerow(headers)


for element in iihs:
    
    # good
    vehicle = (element.find('h1', attrs={
    'class': 'head'}).text)

    # good
    small_overlap_front_drivers_side = ''
    small_overlap_front_drivers_side = element.find(string='Small overlap front: driver-side').parent.parent.find_next_sibling().text.strip()

    # good
    small_overlap_front_passenger_side = ''
    small_overlap_front_passenger_side = element.find(string='Small overlap front: passenger-side').parent.parent.find_next_sibling().text.strip()

    # good
    moderate_overlap_front = ''
    moderate_overlap_front = element.find(string='Moderate overlap front: original test').parent.parent.find_next_sibling().text.strip()

    # good
    side_original = ''
    side_original = element.find(string='Side: original test').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    side_updated_test = ''
    if element.find(string='Side: updated test') == 'true': side_updated_test = element.find(string='Side: updated test')

    # good
    roof_strength = ''
    roof_strength = element.find(string='Roof strength').parent.parent.find_next_sibling().text.strip()

    head_restraints_and_seats = element.find(string='Head restraints & seats').parent.parent.find_next_sibling().text.strip()
    # if element.find(string='Head restraints & seats') == 'true': head_restraints_and_seats = element.find(string='Head restraints & seats').parent.parent.find_next_sibling().text.strip()

    headlight_good = (element.find('span', attrs={'aria-label': 'Good'}).text)

    headlight_acceptable = (element.find('span', attrs={'aria-label': 'Acceptable'}).text)

    headlight_marginal = (element.find('span', attrs={'aria-label': 'Marginal'}).text)
    
    headlight_poor = (element.find('span', attrs={'aria-label': 'Poor'}).text)

    headlights = headlight_good + headlight_acceptable + headlight_marginal + headlight_poor

    # needs testing on page without
    front_crash_prevention_vehicle_to_vehicle = (element.find('div', attrs={'class': 'ca-rating'}))
    # print(front_crash_prevention_vehicle_to_vehicle)

    # needs testing on page without
    front_crash_prevention_vehicle_to_pedestrian_day = (element.find('div', attrs={'class': 'fcp-superior'}).text)

    # needs testing on page without
    front_crash_prevention_vehicle_to_pedestrian_night = ''
    if element.find(string='Front crash prevention: vehicle-to-pedestrian (night)') == 'true': front_crash_prevention_vehicle_to_pedestrian_night = element.find(string='Front crash prevention: vehicle-to-pedestrian (night)').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    seat_belt_reminders = ''
    if element.find(string='Seat belt reminders') == 'true': seat_belt_reminders = element.find(string='Seat belt reminders').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    latch_ease_of_use = ''
    if element.find(string='LATCH ease of use') == 'true': latch_ease_of_use = element.find(string='LATCH ease of use').parent.parent.find_next_sibling().text.strip()

    # vehicle_img here

    file = open('iihs_test.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ([vehicle,
                small_overlap_front_drivers_side,
                small_overlap_front_passenger_side,
                moderate_overlap_front,
                side_original,
                side_updated_test,
                roof_strength,
                head_restraints_and_seats,
                headlights,
                front_crash_prevention_vehicle_to_vehicle,
                front_crash_prevention_vehicle_to_pedestrian_day,
                front_crash_prevention_vehicle_to_pedestrian_night,
                seat_belt_reminders,
                latch_ease_of_use])
    writer.writerow(headers)
    file.close()
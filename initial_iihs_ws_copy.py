import requests, csv
from bs4 import BeautifulSoup

#  check for __iter__ magic method, therefore data is iterable
# print(dir(iihs_index))

url = requests.get('https://www.iihs.org/ratings/vehicle/volkswagen/golf-gti-4-door-hatchback/2022')

soup = BeautifulSoup(url.text, 'html.parser')
# iihs = BeautifulSoup(html_doc, 'html.parser')

iihs = soup.find('div', attrs={'class': 'hero-body'})
print(iihs)

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
            'head_restraints_and_seats',
            'headlights',
            'front_crash_prevtion_vehicle_to_vehicle',
            'front_crash_prevtion_vehicle_to_pedestrian_day',
            'front_crash_prevtion_vehicle_to_pedestrian_night',
            'seat_belt_reminders',
            'latch_ease_of_use',
            ]
writer.writerow(headers)


for element in iihs:

    # good
    vehicle = iihs.find('h1', attrs={'class': 'head'})
    vehicle = vehicle.text

    top_safety_pick = iihs.find('span', attrs={'class': 'tsp'})
    top_safety_pick = top_safety_pick.text
    # top_safety_pick_plus = iihs.find('span', attrs={'class': 'tspPlus'})
    # top_safety_pick_plus = top_safety_pick_plus.text

    # good
    small_overlap_front_drivers_side = ''
    small_overlap_front_drivers_side = iihs.find(string='Small overlap front: driver-side').parent.parent.find_next_sibling().text.strip()

    # good
    small_overlap_front_passenger_side = ''
    small_overlap_front_passenger_side = iihs.find(string='Small overlap front: passenger-side').parent.parent.find_next_sibling().text.strip()

    # good
    moderate_overlap_front = ''
    moderate_overlap_front = iihs.find(string='Moderate overlap front: original test').parent.parent.find_next_sibling().text.strip()

    # good
    side_original = ''
    side_original = iihs.find(string='Side: original test').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    side_updated_test = ''
    if iihs.find(string='Side: updated test') == 'true': side_updated_test = iihs.find(string='Side: updated test')

    # good
    roof_strength = ''
    roof_strength = iihs.find(string='Roof strength').parent.parent.find_next_sibling().text.strip()

    head_restraints_and_seats = iihs.find(string='Head restraints & seats').parent.parent.find_next_sibling().text.strip()
    # if iihs.find(string='Head restraints & seats') == 'true': head_restraints_and_seats = iihs.find(string='Head restraints & seats').parent.parent.find_next_sibling().text.strip()

    headlight_good = (iihs.find('span', attrs={'aria-label': 'Good'}).text)

    headlight_acceptable = (iihs.find('span', attrs={'aria-label': 'Acceptable'}).text)

    headlight_marginal = (iihs.find('span', attrs={'aria-label': 'Marginal'}).text)

    headlight_poor = (iihs.find('span', attrs={'aria-label': 'Poor'}).text)

    headlights = headlight_good + headlight_acceptable + headlight_marginal + headlight_poor

    # needs testing on page without
    front_crash_prevention_vehicle_to_vehicle = iihs.find('a', attrs={'href': '#front-crash-prevention-vehicle-to-vehicle'}).parent.parent
    print(front_crash_prevention_vehicle_to_vehicle)
    print("")

    front_crash_prevention_vehicle_to_vehicle = front_crash_prevention_vehicle_to_vehicle.find_next_sibling()
    print(front_crash_prevention_vehicle_to_vehicle)
    print("")

    print("***")
    front_crash_prevention_vehicle_to_vehicle = front_crash_prevention_vehicle_to_vehicle.find('div', attrs={'class': 'ca-rating'})
    print(front_crash_prevention_vehicle_to_vehicle)
    print("***")

    print("xxx")
    front_crash_prevention_vehicle_to_vehicle = front_crash_prevention_vehicle_to_vehicle.child
    print(front_crash_prevention_vehicle_to_vehicle)
    print("xxx")

    # needs testing on page without
    front_crash_prevention_vehicle_to_pedestrian_day = (iihs.find('div', attrs={'class': 'fcp-superior'}).text)

    # needs testing on page without
    front_crash_prevention_vehicle_to_pedestrian_night = ''
    if iihs.find(string='Front crash prevention: vehicle-to-pedestrian (night)') == 'true': front_crash_prevention_vehicle_to_pedestrian_night = iihs.find(string='Front crash prevention: vehicle-to-pedestrian (night)').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    seat_belt_reminders = ''
    if iihs.find(string='Seat belt reminders') == 'true': seat_belt_reminders = iihs.find(string='Seat belt reminders').parent.parent.find_next_sibling().text.strip()

    # needs testing on page without
    latch_ease_of_use = ''
    if iihs.find(string='LATCH ease of use') == 'true': latch_ease_of_use = iihs.find(string='LATCH ease of use').parent.parent.find_next_sibling().text.strip()

    # vehicle_img here

    file = open('initial_iihs_test.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    content = [vehicle,
            top_safety_pick,
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
            latch_ease_of_use,
            ]
    writer.writerow(content)
    file.close()
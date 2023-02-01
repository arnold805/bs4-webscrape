# for element in iihs:

    # good

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
    front_crash_prevention_vehicle_to_vehicle = element.find('a', attrs={'href': '#front-crash-prevention-vehicle-to-vehicle'}).parent.parent
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
    vehicle_img = title.find_all('img',class_ = "Image_root__J8Wlz Image_lazy__1w_jB Image_loaded__3uNg2 LandingRiver_image__1ZCUb")['src']

    # and if you want the best image quality you could do

    # firstly get the srcset
    vehicle_img = title.find_all('img',class_ = "Image_root__J8Wlz Image_lazy__1w_jB Image_loaded__3uNg2 LandingRiver_image__1ZCUb")['srcset']

    # as srcset is a string but the links are seperated using ',' you could split it on the same
    vehicle_img = vehicle_img.split(',')

    # after splitting the best image quality lik is the last one so get the last element of the new list that you have after splitting
    vehicle_img = vehicle_img[-1]

    # you now have a string with 2x as the unwanted part at the last and you could remove that using the slice operation
    vehicle_img = vehicle_img[:-2]    # slice it upto the third last characterto chop off '2x'

    # now you have a string with leading and trailing spaces so strip it to remove any leading or trailing spaces
    vehicle_img = vehicle_img.strip()
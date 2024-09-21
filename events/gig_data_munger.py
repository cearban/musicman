import json
import pprint

# all_dates = []
# all_data = {}
# new_gig_id = 1
# with open('data/lastfm_gigs.json', 'r') as inpf:
#     data = json.load(inpf)
#     for gig_id in data:
#         gig = data[gig_id]
#         gig_date = gig['gig_date']
#         gig_title = gig['gig_title']
#         gig_lineup = gig['gig_lineup']
#         gig_venue = gig['gig_venue']
#         gig_venue_location_city = gig['gig_venue_location_city']
#         gig_venue_location_country = gig['gig_venue_location_country']
#         all_data[gig_date] = {
#             "gig_date": gig_date,
#             "gig_title": gig_title,
#             "gig_lineup": gig_lineup,
#             "gig_venue": gig_venue,
#             "gig_venue_location_city": gig_venue_location_city,
#             "gig_venue_location_country": gig_venue_location_country
#         }
#         new_gig_id += 1
#
# with open('data/google_cal_gigs.json', 'r') as inpf:
#     data = json.load(inpf)
#     for gig_id in data:
#         gig = data[gig_id]
#         gig_date = gig['gig_date']
#         gig_title = gig['gig_title']
#         gig_lineup = gig['gig_lineup']
#         gig_venue = gig['gig_venue']
#         gig_venue_location_city = gig['gig_venue_location_city']
#         gig_venue_location_country = gig['gig_venue_location_country']
#         all_data[gig_date] = {
#             "gig_date": gig_date,
#             "gig_title": gig_title,
#             "gig_lineup": gig_lineup,
#             "gig_venue": gig_venue,
#             "gig_venue_location_city": gig_venue_location_city,
#             "gig_venue_location_country": gig_venue_location_country
#         }
#         all_dates.append(gig_date)
#         new_gig_id += 1
#
#
# with open('data/lastfm_and_google_cal.json', 'w') as outpf:
#     outpf.write(json.dumps(all_data, indent=4))

sorted_data = {}

with open('../data/lastfm_and_google_cal.json', 'r') as inpf:
    data = json.load(inpf)
    for k in sorted(data.keys()):
        new_gig_date = k[:10]
        sorted_data[new_gig_date] = {
            "gig_title": data[k]["gig_title"],
            "gig_lineup": data[k]["gig_lineup"],
            "gig_venue": data[k]["gig_venue"],
            "gig_venue_location_city": data[k]["gig_venue_location_city"],
            "gig_venue_location_country": data[k]["gig_venue_location_country"]
        }

# with open('data/lastfm_and_google_cal_sorted.json', 'w') as outpf:
#     outpf.write(json.dumps(sorted_data, indent=4))

print(sorted_data)





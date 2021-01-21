#This is where we will transform 

#this is where we will load

import requests
import csv
urldata = "https://api.spacexdata.com/v3/launches"

mission_names = [] 

launch_year = [] 

launch_success = [] 
payload = []
mission_image = []
mission_id = []

def get_launch_data(url):

    launch_data = requests.get(url)
    return launch_data.json()

def transform_data(data):
    for launch in data:
      mission_names.append((launch["mission_name"]))
  #    launch_year.append(launch["launch_year"])
   #   launch_success.append(launch["launch_success"])
      mission_image.append(launch["links"]["mission_patch"])
      mission_id.append(launch["flight_number"])
    # # payload.append(launch)


    with open('flightData.csv', 'w', newline='') as f:
        for a,b,c in zip(mission_id, mission_names, mission_image):

            
                writer = csv.writer(f)
                writer.writerow([a,b,c])

    



result = get_launch_data(urldata)
#print(result)
transform_data(result)
#print(mission_names)
#print(mission_image)
#print(mission_id)
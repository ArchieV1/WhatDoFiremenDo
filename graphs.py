import matplotlib.pyplot as plt
import csv
from collections import Counter
import numpy as np

with open("WhatDoFiremenDo.csv", "r", newline="", encoding="utf") as csv_file:
    Dict = {}
    count = Counter()
    for x, row in enumerate(csv.reader(csv_file, delimiter="%")):
        # If time not in dict of "time:incidents" already, add it
        # row[1][2:4] = First two in XX:YY
        if row[1][2:4] not in Dict.keys():
            Dict[row[1][2:4]] = []

        for incidents in row[2].split("%"):
            for incident in incidents.split(","):
                # Strip the crap
                incident = incident.strip("[").strip("]").strip("\'").replace("\'", "").strip()
                # Add all of the incidents to the Dict of "TIME:[INCIDENTS]"
                Dict[row[1][2:4]].append(incident)

list_of_times = []
list_of_incident_types = []
incident_occurrences = Counter()

for time in Dict.keys():
    list_of_times.append(time)

    Dict[time] = Counter(Dict[time])
    # Dict[time] (Where time = 00, 01 etc) is now a counter obj with "Incident type: Int". Incident type can be
    # multiple incidents separated by a comma eg "'Ambulance, CRT' : Int"
    # Populate the list of incident types for use when generating graph (To be able to call all of them from the Dict)
    for incident_type in list(Dict[time]):
        if incident_type not in list_of_incident_types:
            list_of_incident_types.append(incident_type)
            incident_occurrences[incident_type] = Dict[time][incident_type]
        else:
            incident_occurrences[incident_type] += Dict[time][incident_type]

# Make sure each Counter obj has every option (Or the graph doesn't work)
for time in Dict.keys():
    for incident_type in list_of_incident_types:
        if incident_type not in Dict[time]:
            Dict[time][incident_type] = 0
    print(Dict[time])

print(list_of_incident_types)
print(incident_occurrences)
# Bar chart of incidences/time with incidences grouped by type
plt.ylabel = "Incidents"
plt.xlabel = "Time (24h)"

# The position of the bars on the x-axis
r = [x for x in range(0, 24)]
# Generate all of the bars
fire,  no_info,  false_alarm,  car,  ambulance,  police, forced_entry = [], [], [], [], [], [], []

for time in Dict.keys():
    fire.append(Dict[time]["Fire"])
    no_info.append(Dict[time]["No_Info"])
    false_alarm.append(Dict[time]["False Alarm"])
    car.append(Dict[time]["Car"])
    ambulance.append(Dict[time]["Ambulance"])
    police.append(Dict[time]["Police"])
    forced_entry.append(Dict[time]["Forced entry"])

print(fire)
print(len(no_info))
# Names of the bars
names = ["fire", "no_info", "false_alarm", "car", "ambulance", "police", "forced_entry"]


plt.bar(r, fire)
plt.bar(r, no_info, bottom=fire, color="#111111")

bars = np.add(fire, no_info).tolist
plt.bar(r, false_alarm, bottom=bars, color="#111121")

bars = np.add(bars, false_alarm).tolist
plt.bar(r, car, bottom=bars, color="#113111")

bars = np.add(bars, car).tolist
plt.bar(r, ambulance, bottom=bars, color="#161111")

bars = np.add(bars, ambulance).tolist
plt.bar(r, police, bottom=bars, color="#111911")

bars = np.add(bars, police).tolist
plt.bar(r, forced_entry, bottom=bars, color="#11d111")


plt.xticks(r, names)
plt.show()


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
    print(Dict[time])
    # Populate the list of incident types for use when generating graph (To be able to call all of them from the Dict)
    for incident_type in list(Dict[time]):
        if incident_type not in list_of_incident_types:
            list_of_incident_types.append(incident_type)
            incident_occurrences[incident_type] = Dict[time][incident_type]
        else:
            incident_occurrences[incident_type] += Dict[time][incident_type]
print(list_of_incident_types)
print(incident_occurrences)
# Bar chart of incidences/time with incidences grouped by type
plt.ylabel = "Incidents"
plt.xlabel = "Time (24h)"

# The position of the bars on the x-axis
r = [x for x in range(0, 25)]

# Generate all of the bars
print("\n")

# for incident_type in list_of_incident_types:
#     bar_data = []
#     for time in Dict.keys():
#         if incident_type in list(Dict[time]):
#             bar_data.append(Dict[time][incident_type])
#         else:
#             bar_data.append(0)
#     print(incident_type)
#     print(bar_data)
#     plt.bar(r, bar_data, width=1)


plt.show()

import yaml
import json
import datetime

with open('/home/jacob/Downloads/hack-cambridge-sponsors-portal-export.json') as f:
    workshop_file_name = 'workshops' + datetime.datetime.today().strftime('%Y-%m-%d') + '.yml'
    with open(workshop_file_name, 'w') as workshop_file:
        workshop_entries = []
        data = json.load(f)
        sponsors = data["sponsors"]
        count = 0
        for _, sponsor in sponsors.items():
            if "workshop" in sponsor:
                workshop = sponsor['workshop']
                workshop_entry = dict()
                workshop_entry["name"] = workshop["title"]
                workshop_entry["description"] = workshop["description"]
                workshop_entry["time"] = ""
                workshop_entries.append(workshop_entry)

            workshops = {"workshops": workshop_entries}
        yaml.dump(workshops, workshop_file, default_flow_style=False)

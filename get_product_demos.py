import yaml
import json
import datetime

with open('/home/jacob/Downloads/hack-cambridge-sponsors-portal-export.json') as f:
    demo_file_name = 'demos' + datetime.datetime.today().strftime('%Y-%m-%d') + '.yml'
    with open(demo_file_name, 'w') as demo_file:
        demo_entries = []
        data = json.load(f)
        sponsors = data["sponsors"]
        count = 0
        for _, sponsor in sponsors.items():
            if 'doingDemo' in sponsor:
                print(sponsor['name'], sponsor['doingDemo'])
            if "demo" in sponsor:
                demo = sponsor['demo']
                demo_entry = dict()
                demo_entry["name"] = demo["title"]
                demo_entry["description"] = demo["description"]
                demo_entry["time"] = ""
                demo_entries.append(demo_entry)

            demos = {"demos": demo_entries}
        yaml.dump(demos, demo_file, default_flow_style=False)

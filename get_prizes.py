import yaml
import json
import datetime

with open('/home/jacob/Downloads/hack-cambridge-sponsors-portal-export.json') as f:
    prize_file_name = 'prizes' + datetime.datetime.today().strftime('%Y-%m-%d') + '.yml'
    with open(prize_file_name, 'w') as prize_file:
        prize_entries = []
        data = json.load(f)
        sponsors = data["sponsors"]
        count = 0
        for _, sponsor in sponsors.items():
            if "competitions" in sponsor:
                competitions = sponsor['competitions']
                if competitions["doingHardwareApiCompetition"]:
                    print("Product")
                    hardwareApiCompetition = competitions["hardwareApiCompetition"]
                    prize_entry = dict()
                    prize_entry["name"] = hardwareApiCompetition["title"]
                    prize_entry["description"] = hardwareApiCompetition["description"]
                    prize_entry["prize"] = hardwareApiCompetition["prizes"]
                    prize_entries.append(prize_entry)
                if competitions["doingThemedCompetition"]:
                    print("Themed")
                    themedCompetition = competitions["themedCompetition"]
                    prize_entry = dict()
                    prize_entry["name"] = themedCompetition["title"]
                    prize_entry["description"] = themedCompetition["description"]
                    prize_entry["prize"] = themedCompetition["prizes"]
                    prize_entries.append(prize_entry)

            prizes = {"prizes": prize_entries}
        yaml.dump(prizes, prize_file, default_flow_style=False)

import json


with open('/home/jacob/Downloads/hack-cambridge-sponsors-portal-export.json') as f:
    data = json.load(f)
    sponsors = data["sponsors"]
    count = 0
    for _, sponsor in sponsors.items():
        if sponsor["tier"] == "Giga":
            print("Sponsor: ", sponsor["name"])
            if "people" in sponsor:
                people = sponsor["people"]
                if "mentors" in people:
                    mentors = people["mentors"]
                    for p in mentors:
                        if p is not None:
                            print("Name: ", p.get("name", ""))
                            print("Email: ", p.get("email", ""))
                            print("Phone: ", p.get("phone", ""))
                            count += 1

                if "recruiters" in people:
                    recruiters = people["recruiters"]
                    for p in recruiters:
                        if p is not None:
                            print("Name: ", p.get("name", ""))
                            print("Email: ", p.get("email", ""))
                            print("Phone: ", p.get("phone", ""))
                            count += 1
                print("")
    print("Total attending: ", count)
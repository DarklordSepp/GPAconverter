import json
with open('Strings.json', 'r',) as strings_json:
    Strings = json.load(strings_json)

print(Strings['desktopDir'])
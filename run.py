import json,toml,re

base_toml_file = "base.toml"
allowlist_toml_file = "allowlist.toml"

with open(base_toml_file) as source:
    base_config = toml.loads(source.read())

with open(allowlist_toml_file) as source:
    allowlist_config = toml.loads(source.read())

base_json_config = json.loads(json.dumps(base_config))
for base in base_json_config['rules']:
    if not 'description' in base:
        print("The description field is missing in base file")
        exit(1)
    if re.match("Rule (\d+):", base['description']) == None:
        print("The description field is missing rule parameter in base file, here: ", base['description'])
        exit(2)

allowlist_json_config = json.loads(json.dumps(allowlist_config))
for entry in allowlist_json_config['rules']:
    if not 'id' in entry:
        print("id parameter is missing in allowlist")
        exit(3)
    if not entry['id'].isdigit():
        print("id is not an integer in allowlist")
        exit(4)

# Rule specific allowlist rule set
for i,entry in enumerate(allowlist_json_config['rules']):
    for j,base in enumerate(base_json_config['rules']):
        # print(re.match("Rule (\d+):", base['description']))
        base_id = re.match("Rule (\d+):", base['description']).groups()[0]
        if entry['id'] == base_id:
            base_json_config['rules'][j]['allowlist'] = entry['allowlist']

# Global allowlist rule set
if allowlist_json_config['allowlist']:
    base_json_config['allowlist'] = allowlist_json_config['allowlist']

# Generate final toml rule set
toml_config = toml.dumps(base_json_config)
print(toml_config)

import json,toml

base_toml_file = "base.toml"
allowlist_toml_file = "allowlist.toml"

with open(base_toml_file) as source:
    base_config = toml.loads(source.read())

with open(allowlist_toml_file) as source:
    allowlist_config = toml.loads(source.read())

base_json_config = json.loads(json.dumps(base_config))
allowlist_json_config = json.loads(json.dumps(allowlist_config))

# Rule specific allowlist rule set
for i,entry in enumerate(allowlist_json_config['rules']):
    for j,base in enumerate(base_json_config['rules']):
        if entry['id'] == base['id']:
            base_json_config['rules'][j]['allowlist'] = entry['allowlist']

# Global allowlist rule set
if allowlist_json_config['allowlist']:
    base_json_config['allowlist'] = allowlist_json_config['allowlist']

# Generate final toml rule set
toml_config = toml.dumps(base_json_config)
print(toml_config)

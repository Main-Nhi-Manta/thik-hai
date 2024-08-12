import requests
import json
import re

# Fetch the JSON data from the API
response = requests.get('https://fox.toxic-gang.xyz/tata/channels')
input_json = response.json()

# Extract the relevant data from the JSON response
data = input_json['data']

# Function to perform replacements
def replace_urls(channel):
    if 'initialUrl' in channel:
        # Replace delta and bpweb with bpprod and tatasky.akamaized.net with catchup.akamaized.net
        url = channel['initialUrl'].replace('delta', 'bpprod').replace('bpwta', 'bpprod').replace('tatasky.akamaized.net', 'catchup.akamaized.net')
        # Replace <number>.akamaized.net with catchup.akamaized.net preserving the number
        url = re.sub(r'(\d+)\.akamaized\.net', r'\1catchup.akamaized.net', url)
        # Replace the ending with xxx.mpd
        url = re.sub(r'[a-zA-Z0-9]+\.mpd$', 'dtvhindi.mpd', url)
        channel['initialUrl'] = url
    return channel

# Replace URLs in all channels
customized_channels = [replace_urls(channel) for channel in data]

# Prepare the final output format
output_json = {}
for channel in customized_channels:
    if 'licence1' in channel and 'licence2' in channel:
        key_info = {
            'clearkey': f"{channel['licence1']}:{channel['licence2']}",
            'url': channel['initialUrl']
        }
        output_json[channel["id"]] = key_info

# Save the output to a JSON file
with open('pta_nhi.json', 'w') as outfile:
    json.dump(output_json, outfile, indent=2)

# Print the result
print("File Saved Successfully")

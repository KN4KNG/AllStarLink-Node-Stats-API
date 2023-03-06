import sys
import requests

# Check if user provided a command line argument for node
if len(sys.argv) > 1:
    node = sys.argv[1]
    # Check if node is a valid integer
    try:
        int(node)
    except ValueError:
        print("Error: Node number must be an integer")
        exit()
else:
    # Prompt the user to enter a node number
    node = input("Enter a node number (e.g. 504851): ").strip()
    if not node:
        print("Node number cannot be empty")
        exit()

# Make an API request to AllStarLink
url = f"https://stats.allstarlink.org/api/stats/{node}"
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Error:", response.status_code)
    exit()

# Get the data from the response
data = response.json()

# Print the data in an organized manner
print("Node ID:", data["stats"]["id"])
print("Node:", data["stats"]["node"])
print("Uptime (seconds):", data["stats"]["data"]["apprptuptime"])
print("Version:", data["stats"]["data"]["apprptvers"])
print("Linked nodes:", ", ".join(data["stats"]["data"]["nodes"].split(",")))
print("Linked node IDs:")
for node_info in data["stats"]["data"]["linkedNodes"]:
    try:
        print(f"{node_info['name']}: {node_info['Node_ID']}")
    except KeyError:
        print(f"Linked node ID not available for node {node_info['name']}")
print("Keyed:", "Yes" if data["stats"]["data"]["keyed"] else "No")
print("Keyup count:", data["stats"]["data"]["totalkeyups"])
print("Transmit time (seconds):", data["stats"]["data"]["totaltxtime"])

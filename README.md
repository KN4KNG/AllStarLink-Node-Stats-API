
# AllStarLink Node Stats API

This Python script retrieves and displays statistics for a specified node using the AllStarLink Node Stats API.

## Usage

To use this script, simply run it from the command line, optionally passing in the node number as a command line argument. If the node number is not provided as a command line argument, the script will prompt the user to enter it.

`python node_stat_api.py [node_number]` 

## Requirements

-   Python 3.x
-   `requests` library (can be installed via pip)

## Output

The script will output the following information for the specified node:

-   Node ID
-   Node number
-   Uptime (seconds)
-   Version
-   Linked nodes
-   Linked node IDs (if available)
-   Keyed status
-   Keyup count
-   Transmit time (seconds)

## Example Output

    Node ID: 22242
    Node: 504851
    Uptime (seconds): 370479
    Version: 2.0
    Linked nodes: T1999, TKN4KNGZello-P, TKN4KNG
    Linked node IDs:
    Linked node ID not available for node 1999
    Linked node ID not available for node KN4KNGZelloP
    Linked node ID not available for node KN4KNG
    Keyed: No
    Keyup count: 19
    Transmit time (seconds): 295

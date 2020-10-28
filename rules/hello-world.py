# ruleid:hello-world
5 == 5

# ok:hello-world
7 == 8

# ruleid:hello-world
if "cat" == "cat":
    print("equal pets")

# ruleid:hello-world
if a.id + string(len(arr)) == a.id + string(len(arr)):
    print("equal IDs")

def compare_nodes(arr, node_id):
    # ruleid:hello-world
    matched = [x for x in arr if x.node_id == x.node_id ]
    return matched

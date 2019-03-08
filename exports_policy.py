from function import *
from var import *
import os
import shutil

counter = 0

p_exported = 0

os.mkdir(export_path)

total_count = getTotalCount(src_nodeName, src_port, src_auth_values, src_https, verify)

while counter < counter_max:
    
    counter += 1
    policy = getPoliciesId(src_nodeName, src_port, src_auth_values, src_https, counter, verify)
    #counter += 1

    if policy.get('statusCode'):

        print("[" + str(counter) + "/" + str(counter_max) + "] no policy available for this ID")

    else:

        print("[" + str(counter) + "/" + str(counter_max) + "] Exporting policy : " + policy["service"] + " " + str(policy["name"]))

        # Name the JSON file after the service which the policy belong and the policy ID
        export_file = export_path + "/" + policy["service"] + "_" + str(policy["id"]) + ".json"

        # Open the file
        with open(export_file, 'w') as outfile:

            # dump the Json content into the file
            json.dump(policy, outfile)
        p_exported += 1
if p_exported > 0:

    # Creating the archive with all the policies
    print("Creation of the archive")

    shutil.make_archive(export_path, 'zip', export_path)

    print("Archive ready : " + export_path + ".zip")

# Deleting the staging file and directory
shutil.rmtree(export_path)

print("Total policies available in Ranger instance " + src_nodeName + ": " + str(total_count))

print("Total policies exported : " + str(p_exported))

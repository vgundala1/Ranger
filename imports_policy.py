from var import *
from function import *
from os import listdir
from pprint import pprint
import json
import urllib3
import shutil

# Initiate counting variables
total_policies = 0
import_success = 0
import_failed = 0

# Initiate result dict :
# Imported_policies is used to store successfully imported policies with the format : { policy_filename.json : success }
# Failed_policies is used to store failed import policies with the format : { policy_filename.json : error_msg }
imported_policies = {}
failed_policies = {}

# Disable warning due to self signed certificates
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Unarchive the zip file exported by export script
shutil.unpack_archive(export_path + ".zip", export_path)


for filename in listdir(export_path):

    # Store the total of policies handled by the script
    total_policies += 1

    # Open the file
    policy_file = open(export_path + "/" + filename, "r")

    # read the file store it
    content = policy_file.read()

    # Parse the file and type it as JSON
    policy_json = json.loads(content)

    # As python load JSON with simple quote, using dumps to reformat the json with double quote
    policy_json_clean = json.dumps(policy_json)

    # Import the file in ranger
    ranger_import = importPolicies(dst_nodeName, dst_port, policy_json_clean, dst_auth_values, dst_https, verify)

    # If the policy is well imported, the return will describe the policy itself.
    # As the ID is part of the policy body, if we can see this property in the return, i
    # it mean that the policy is imported
    if ranger_import.get('id'):

        imported_policies.update({filename: "success"})

        import_success += 1

        print("[" + str(total_policies) + "] policy" + filename + "imported successfully")

    else:

        failed_policies.update({filename: ranger_import["msgDesc"]})

        import_failed += 1

        print("[" + str(total_policies) + "] ERROR policy" + filename + "failed to import")

print("Policies handled by the script :" + str(total_policies))
print("Successfully imported policy: " + str(import_success))
print("Failed policy import :" + str(import_failed))
print("")

print(failed_policies)

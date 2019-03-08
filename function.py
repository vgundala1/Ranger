import requests
import json
import urllib3

# Disable untrusted CA warning when connecting in HTTPS with self certificate
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Get the number of policies to control the export
def getTotalCount(nodeName, port, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/service/public/api/policy"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/service/public/api/policy"

    else:

        exit("[getServices] could not run because of : bad value provided. Please check the http var")


    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7a5cdb20-017b-46aa-92c1-00ee983654db"
        }

    response = requests.request("GET", url, headers=headers, auth=auth_values, verify=verify)

    # API response is JSON formatted, so we load and return the result as JSON data.
    total_policies = json.loads(response.text)
    high = total_policies['vXPolicies']
    #print (high)
    for i in range(len(high)):
       print (max(["id"]))
    return total_policies["totalCount"]


# Retrieve all Ranger services (hadoop, yarn, hbase, etc) for a given Ranger instance.
def getServices(nodeName, port, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/service/public/v2/api/service"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/service/public/v2/api/service"

    else:

        exit("[getServices] could not run because of : bad value provided. Please check the https var")


    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7a5cdb20-017b-46aa-92c1-00ee983654db"
        }

    response = requests.request("GET", url, headers=headers, auth=auth_values, verify=verify)

    # API response is JSON formatted, so we load and return the result as JSON data.
    services = json.loads(response.text)

    return services


# Retrieve policy by ID
def getPoliciesId(nodeName, port, auth_values, https, id, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/service/public/v2/api/policy/" + str(id)

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/service/public/v2/api/policy/" + str(id)

    else:

        exit("[getPolicies] could not run because of : bad value provided. Please check the https var")


    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "655a773b-1b92-4984-90fb-a13e1125268b"
        }

    response = requests.request("GET", url, headers=headers, auth=auth_values, verify=verify)

    # API response is JSON formatted, so we load and return the result as JSON data.
    policies_id = json.loads(response.text)
    return policies_id


# Retrieve all Ranger policies for a given Ranger service
def getPolicies(nodeName, port, auth_values, https, serviceName, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/service/plugins/policies/download/" + serviceName

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/service/plugins/policies/download/" + serviceName

    else:

        exit("[getPolicies] could not run because of : bad value provided. Please check the https var")

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "655a773b-1b92-4984-90fb-a13e1125268b"
        }

    response = requests.request("GET", url, headers=headers, auth=auth_values, verify=verify)

    # API response is JSON formatted, so we load and return the result as JSON data.
    service_policies = json.loads(response.text)

    return service_policies


def importPolicies(nodeName, port, payload, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/service/public/v2/api/policy/"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/service/public/v2/api/policy/"

    else:

        exit("[getPolicies] could not run because of : bad value provided. Please check the https var")

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2da99a97-060b-433f-89e1-cbb34d47974c"
    }

    response = requests.request("POST", url, data=payload, headers=headers, auth=auth_values, verify=verify)

    import_policies = json.loads(response.text)

    return import_policies

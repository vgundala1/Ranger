This scripts used to export and import the ranger policies.
You need to modify var.py file with correct ranger hosts,username,password etc and change max policy number as per the source ranger policy numbers.
Run export.py which exports all policies in JSON format and compress it with zip.
Run import.py import all the policies to destination ranger hosts.
Note: This scripts expects same service ranger plugin names (for all services like hdfs,yarn etc) in source and destination ranger, TIP: change the destnation service plugin names to match source ranger UI, once you successfuly migrated policies you can revert the changes. You can change service names in Ranger UI iteself for each plugin.



This scripts requires python3 to be installed.

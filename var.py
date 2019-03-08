######################
# SOURCE CLUSTER VAR #
######################

# Ranger user with necessary rights to request services and alerts status
src_user = "admin"

# user password
src_passwd = "admin"

# use for iterate over policies id. Put the highest value of your policies ID.
counter_max = 11

# resolvable name of the Ranger server
src_nodeName = "10.42.17.17"

# auth token for the api, do not touch unless if necessary
src_auth_values = (src_user, src_passwd)

# the port where Ranger Admin is listening
src_port = "6080"

# if Ranger is configured in https put "y" if not, put "n"
src_https = "n"

###########################
# DESTINATION CLUSTER VAR #
###########################

# Ranger user with necessary rights to request services and alerts status
dst_user = "admin"

# user password
dst_passwd = "Test@123"

# resolvable name of the Ranger server
dst_nodeName = "10.42.17.152"

# auth token for the api, do not touch unless if necessary
dst_auth_values = (dst_user, dst_passwd)

# the port where Ranger Admin is listening
dst_port = "6080"

# if Ranger is configured in https put "y" if not, put "n"
dst_https = "n"

##############
# GLOBAL VAR #
##############

verify = False

# the output of run_export and the input of run_import
export_path = "/Users/vinod.gundala/exports"

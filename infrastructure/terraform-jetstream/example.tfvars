###########################################
# Brock Palen
# brockp@umich.edu
# http://arc-ts.umich.edu/

################
##
#  Example tfvars file, you can change any variable in inputs.tf here

###############################################################################
## Jetstream VM options

# number of VM's to start
quantity = "4"


##  Image ID to startup
##  JS-API-Featured-Ubuntu18-Feb-14-2020 
image_id = "0d13b72c-db35-439f-9118-2946148eb5c6"
image_name = "JS-API-Featured-Ubuntu18-Feb-14-2020"

##  VM Flavor to startup: https://jetstream-cloud.org/tech-specs/cloud-services.php
##  Controls CPU / Memory footprint
vm_flavor = "m1.quad"

#VM name
vm-name = "Squadron"

##  SSH Keypair control
keypair-name = "Squadron-keypair"


###############################################################################
##
#  Network options

secgroup = "Squadron-global-ssh"

internal-network = {
   network-name = "Squadron-api-net"
   subnet-name = "Squadron-api-subnet1"
   subnet-cidr = "10.0.0.0/24"
   router-name = "Squadron-api-router"
   ##  Check how to set external gateway here
   external-gateway = "4367cd20-722f-4dc2-97e8-90d98c25f12e"
}

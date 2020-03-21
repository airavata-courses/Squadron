###########################################
# Brock Palen
# brockp@umich.edu
# http://arc-ts.umich.edu/

resource "openstack_networking_floatingip_v2" "floatip_1" {
  count = "${var.quantity}"
  pool  = "public"
}

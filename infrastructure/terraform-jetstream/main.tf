###########################################
# Brock Palen
# brockp@umich.edu
# http://arc-ts.umich.edu/

provider "openstack" {}

resource "openstack_compute_keypair_v2" "keypair" {
  name       = "${var.keypair-name}"
  public_key = "${file("${var.keypair-path}")}"
}

resource "openstack_compute_instance_v2" "servers" {
  count           = "${var.quantity}"
  name            = "${var.vm-name}-${count.index}"
  image_id        = "${var.image_id}"
  flavor_name     = "${var.vm_flavor}"
  key_pair        = "${openstack_compute_keypair_v2.keypair.name}"
  key_pair        = "${var.keypair-name}"
  security_groups = ["${var.secgroup}"]

  network {
    name = "${var.internal-network["network-name"]}"
  }
}

resource "openstack_compute_floatingip_associate_v2" "myip" {
  count       = "${var.quantity}"
  floating_ip = "${element(openstack_networking_floatingip_v2.floatip_1.*.address, count.index)}"
  instance_id = "${element(openstack_compute_instance_v2.servers.*.id, count.index)}"
}

resource "openstack_blockstorage_volume_v3" "volumes" {
  count       = "${var.quantity}"
  name        = "${var.vm-name}-${count.index}"
  size        = "${var.volume-size}"
}

resource "openstack_compute_volume_attach_v2" "attachvolume" {
  count       = "${var.quantity}"
  volume_id = "${element(openstack_blockstorage_volume_v3.volumes.*.id, count.index)}"
  instance_id = "${element(openstack_compute_instance_v2.servers.*.id, count.index)}"
}

output "server_ips" {
  value = "${openstack_compute_floatingip_associate_v2.myip.*.floating_ip}"
}

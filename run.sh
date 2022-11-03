#!/bin/bash

memory="-m 1G"
spice="-device virtio-serial -chardev spicevmc,id=vdagent,debug=0,name=vdagent -device virtserialport,chardev=vdagent,name=com.redhat.spice.0"
net="-nic user -nic tap,helper=/usr/lib/qemu/qemu-bridge-helper"
vga="-vga qxl"
display="-display spice-app,gl=on"
disk="astra.qcow2"

if [[ $(ip a | grep -o br0:) != "br0:" ]]; then
  nmcli c up br0
fi

while [[ -n $1 ]]; do
  case $1 in
    -m) memory="-m $2"; shift;;
    -c) cdrom="-cdrom $2"; shift;;
    -d) display="-display $2"; shift;;
    -v) vga="-vga $2"; shift;;
    -b) boot="-boot once=d -cdrom $3"; shift;;
    *.qcow2) disk="$1"
  esac
  shift
done
if [[ $boot ]]; then
  qemu-system-x86_64  -accel kvm -cpu host -smp 2 $display $vga $memory $boot $disk
elif [[ $cdrom ]]; then
  qemu-system-x86_64  -accel kvm -cpu host -smp 2 $display $vga $net $spice $memory $cdrom $disk
else
  qemu-system-x86_64  -accel kvm -cpu host -smp 2 $display $vga $net $spice $memory $disk
fi

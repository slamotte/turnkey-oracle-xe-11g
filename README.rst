TurnKey Oracle XE 11g
==================================================

This is `Oracle Database 11g Express Edition
<http://www.oracle.com/technetwork/products/express-edition/overview/index.html>`_
`virtual appliance <http://en.wikipedia.org/wiki/Virtual_appliance>`_. A
virtual appliance is a virtual machine image designed to run on a
virtualization platform.

The appliance is based on `TurnKey Core <http://www.turnkeylinux.org/core>`_
that provides a small footprint Linux server tailored for virtual appliance
use. The appliance doesn't include Oracle XE out of the box because of unclear
licensing issue but provides a ready-made environment where the installation
of Oracle is easy to do by following these instructions.

The instructions are targetted to `VirtualBox <https://www.virtualbox.org/>`_
installation as it's the only virtualization environment were I have run the
appliance so far.

The high level steps are:

1. set up a VirtualBox virtual machine (or any other virtualization platform)
2. log in to virtual machine and install and configure Oracle

Resources
--------------------------------------------------

- `Oracle Database 11g Express Edition <http://www.oracle.com/technetwork/products/express-edition/overview/index.html>`_
- `Oracle Database Express Edition 11g Release 2 download page <http://www.oracle.com/technetwork/products/express-edition/downloads/index.html>`_
- `Oracle Database Express Edition Installation Guide for Linux x86-64 <http://docs.oracle.com/cd/E17781_01/install.112/e18802/toc.htm>`_
- `Ask Ubuntu <http://askubuntu.com>`_: `How to install Oracle Express 11gR2? <http://askubuntu.com/questions/198163/how-to-install-oracle-express-11gr2>`_
- `Installing Oracle 11g R2 Express Edition on Ubuntu 64-bit <http://meandmyubuntulinux.blogspot.fi/2012/05/installing-oracle-11g-r2-express.html>`_
- `Oracle 11g AMM: MEMORY_TARGET, MEMORY_MAX_TARGET and /dev/shm <http://blog.oracle48.nl/oracle-11g-amm-memory_target-memory_max_target-and-dev_shm/>`_
- `VirtualBox <https://www.virtualbox.org/>`_

Virtual Machine Setup
--------------------------------------------------

Set the following parameters for the new virtual machine:

- Memory: 2GB
- Disk size: 20GB (there will be 16GB free space after installation)
- Network adapter: Bridged (so you can access it from anywhere on your network)

If you need more disk space just increase the disk size as much as you like.

2GB memory is probably too much as according to Oracle documents XE uses 1 GB
at maximum. But OTOH 2GB RAM creates enough swap to fullfill Oracle's swap
requirement.

How to build your ISO
--------------------------------------------------

First get the zipped Oracle XE RPM package from `Oracle site <http://www.oracle.com/technetwork/products/express-edition/downloads/index.html>`.
Unzip it and convert to a Debian package like so:

::

    unzip oracle-xe-11.2.0-1.0.x86_64.rpm.zip
    alien --scripts Disk1/oracle-xe-11.2.0-1.0.x86_64.rpm

Copy the resultant deb (e.g. oracle-xe_11.2.0-2_amd64.deb) to overlay/root/ and
update the constant at the top of /overlay/usr/lib/inithooks/41oracle accordingly.
Then build your ISO:

::

    make

That's it. Set your new VM to boot from this ISO and after a couple minutes you'll
have a fully-functioning Oracle XE instance. From an external machine you can log
in using sqlplus:

::

    sqlplus system/password@ipaddress/xe

Create an Oracle user account:

::

    root@turnkey-oracle-xe-11g ~# $ORACLE_HOME/bin/sqlplus sys/<PASSWORD> as
    sysdba @bin/mkorauser.sql <USERNAME> <PASSWORD>

#!/usr/bin/python
"""Set Oracle XE SYS-user password for silent installation

Option:
--dbpass= unless provided, will ask interactively
"""

import sys
import getopt

from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'dbpass='])
    except getopt.GetoptError, e:
        usage(e)

    dbpassword = ""
    
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--dbpass':
            dbpassword = val

    if not dbpassword:
        d = Dialog('TurnKey Linux - First boot configuration')
        dbpassword = d.get_password(
            "Oracle XE SYS Password",
            "Enter new password for the Oracle XE SYS-user.")

    with open("/root/oracle.rsp", "w") as text_file:
        text_file.write("""###############################################################################
#                                                                             #
# HTTP port that will be used to access APEX admin page                       #
# Default : 8080                                                              #
#                                                                             #
###############################################################################
ORACLE_HTTP_PORT=8080

###############################################################################
#                                                                             #
# TNS port that will be used to configure listener                            #
# Default : 1521                                                              #
#                                                                             #
###############################################################################
ORACLE_LISTENER_PORT=1521

###############################################################################
#                                                                             #
# Passwords can be supplied for the following two schemas in the              #
# starter database:                                                           #
#   SYS                                                                       #
#   SYSTEM                                                                    #
#                                                                             #
###############################################################################
ORACLE_PASSWORD=%(dbpassword)s

###############################################################################
#                                                                             #
# Passwords can be supplied for the following two schemas in the              #
# starter database:                                                           #
#   SYS                                                                       #
#   SYSTEM                                                                    #
#                                                                             #
#   ORACLE_CONFIRM_PASSWORD should be same as ORACLE_PASSWORD                 #
#                                                                             #
###############################################################################
ORACLE_CONFIRM_PASSWORD=%(dbpassword)s

###############################################################################
#                                                                             #
# To start/stop listener and database instance up on system boot              #
#                                                                             #
###############################################################################
ORACLE_DBENABLE=y
""" % {'dbpassword': dbpassword})

if __name__ == "__main__":
    main()

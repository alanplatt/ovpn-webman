from subprocess import Popen, PIPE, STDOUT
from pathlib import Path
import re
import pexpect


def create_vpn_cert(user, password, capassword):
    try:
        child = pexpect.spawn("easyrsa build-client-full {}".format(user))
        child.expect('Enter PEM pass phrase:', timeout=60)
        child.sendline(password)
        child.sendline(password)
        child.expect('Enter pass phrase for /etc/openvpn/pki/private/ca.key:', timeout=60)
        child.sendline(capassword)
    except:
        print("error creating certificate")
        raise


def get_vpn_cert(user):
    try:
        cert_p = Popen(['ovpn_getclient', user], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate()[0]
        return cert_p.decode()
    except:
        raise


def check_if_user_has_cert(user):
    cert_file = Path("/etc/openvpn/pki/private/{}.key".format(user))
    if cert_file.is_file():
        return True
    return False


def check_password(password):
    if len(password) < 8:
        return False
    if re.search('[A-Z]', password) is None:
        return False
    if re.search('[0-9]', password) is None:
        return False

    return True

#############################################################################
# FS
#
# Module contains an implementation of SONiC PSU Base API and
# provides the PSUs status which are available in the platform
#
#############################################################################

import os.path

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError(str(e) + "- required module not found")


class PsuUtil(PsuBase):
    """Platform-specific PSUutil class"""

    def __init__(self):
        PsuBase.__init__(self)

        self.psu_path = "/sys/bus/i2c/devices/"
        self.psu_presence = "/psu_present"
        self.psu_oper_status = "/psu_power_good"
        self.psu_mapping = {
            2: "10-0051",
            1: "9-0050",
        }

    def get_num_psus(self):
        return len(self.psu_mapping)

    def get_psu_status(self, index):
        if index is None:
            return False

        status = 0
        node = self.psu_path + self.psu_mapping[index]+self.psu_oper_status
        try:
            with open(node, 'r') as power_status:
                status = int(power_status.read())
        except IOError:
            return False

        return status == 1

    def get_psu_presence(self, index):
        if index is None:
            return False

        status = 0
        node = self.psu_path + self.psu_mapping[index] + self.psu_presence
        try:
            with open(node, 'r') as presence_status:
                status = int(presence_status.read())
        except IOError:
            return False

        return status == 1

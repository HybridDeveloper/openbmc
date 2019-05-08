#!/usr/bin/env python
#
# Copyright 2018-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

from common.base_kernel_module_presence_test import BaseKernelModulePresenceTest

class KernelModulePresenceTest(BaseKernelModulePresenceTest):

    def set_kmods(self):
        self.expected_kmod = [
              "usb_f_acm",
              "u_serial",
              "usb_f_ecm",
              "g_cdc",
              "u_ether",
              "libcomposite",
              "configfs",
              "tun",
              "ast_adc",
              "adm1275",
              "max127",
              "lm75",
              "pmbus",
              "at24",
              "pfe1100",
              "pmbus_core",
              "fb_panther_plus"
        ]
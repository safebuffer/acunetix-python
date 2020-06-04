# -*- coding: utf-8 -*-
import sys
from acunetix import Acunetix

server = Acunetix(host="", api="")

server.delete_all_targets()
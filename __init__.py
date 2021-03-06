import os, sys, inspect, platform

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir+"/simple_emulator")
# print(sys.path)

from objects.emulator import PccEmulator
from objects.cc_base import CongestionControl
from player.packet_selection import Solution as Packet_selection
from utils import *
from config.constant import *
from config import constant

from player.examples.reno import Reno
# from player.examples.simple_bbr import BBR
# from player.examples.RL import RL
from double_flow import create_2flow_emulator
from qoe_model import cal_qoe

# from scripts.block_trace_generator import generate_block_trace
# from scripts.network import create_network, create_trace


__all__ = ["PccEmulator", "CongestionControl", "Packet_selection", \
           "analyze_pcc_emulator", "plot_cwnd", "plot_rate", \
           "Reno", "create_2flow_emulator", "constant", \
           "cal_qoe"]

try:
    if os.path.exists("output"):
        if platform.system() == "Windows":
            # for windows
            os.system("rmdir /Q /S output")
        else:
            # for linux
            os.system("rm -rf output")

    # os.rmdir("output")
    os.mkdir("output")
    os.mkdir("output/packet_log")

except Exception as e:
    pass

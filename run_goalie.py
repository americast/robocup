KUB_ID = 0

import rospy,sys
from utils.geometry import Vector2D
from utils.functions import *
from krssg_ssl_msgs.msg import point_2d
from krssg_ssl_msgs.msg import BeliefState
from krssg_ssl_msgs.msg import gr_Commands
from krssg_ssl_msgs.msg import gr_Robot_Command
from krssg_ssl_msgs.msg import BeliefState
from multiprocessing import Process
from kubs import kubs
from math import atan2,pi
from utils.functions import *

from tactics import  Goalie

pub = rospy.Publisher('/grsim_data',gr_Commands,queue_size=1000)

import memcache
shared = memcache.Client(['127.0.0.1:11211'],debug=False)
# _Goalie_.main()
flag = True
kub = kubs.kubs(0,pub)
def function(id_,state):
	# global flag
	# print(kub.kubs_id)
	g_fsm = Goalie.Goalie()
	# print(kub.kubs_id+1)
	g_fsm.add_kub(kub)
	# print(kub.kubs_id+2)

	# g_fsm.as_graphviz()
	# g_fsm.write_diagram_png()
	g_fsm.spin()
	# print(kub.kubs_id+3)


rospy.init_node('goalie',anonymous=False)
start_time = rospy.Time.now()

start_time = 1.0*start_time.secs + 1.0*start_time.nsecs/pow(10,9)   



while True:
	state = shared.get('state')
	if state:
		kub.update_state(state)
		function(KUB_ID,state)
		


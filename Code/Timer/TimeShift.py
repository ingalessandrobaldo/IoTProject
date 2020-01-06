import json
import datetime
import socket
import requests

class TimeShift(object):
	def __init__(self):
		self.scheduling={
		"2":[],
		"3":[],
		"4":[],
		"5":[],
		}

		self.catalog="http://192.168.1.102:8080"
		self.my_data={
		"time_shift":
		{	
		"ip":socket.gethostbyname(socket.gethostname()),
		"port":8087
		}
		}


	def configure(self):
		self.result=requests.post(self.catalog,json.dumps(self.my_data))
		self.ip_others=self.result.json()
		print(json.dumps(self.ip_others,indent=4))

	def sendAlert(self):

		for key in self.scheduling.keys():
			if(key=="2"):
				for elem in scheduling[key]:
					if(time.time()-elem["last_measurement"]>=60):
						r=requests.get("http://"+self.ip_others["queue_server"][0]+":"+self.ip_others["queue_server"][1]+"/retrieve?pressure_id="+elem["pressure_id"]+"&heart_id="+elem["heart_id"]+"&glucose_id="+elem["glucose_id"])
			elif(key=="3"):
				for elem in scheduling[key]:
					if(time.time()-elem["last_measurement"]>=240):
						r=requests.get("http://"+self.ip_others["queue_server"][0]+":"+self.ip_others["queue_server"][1]+"/retrieve?pressure_id="+elem["pressure_id"]+"&heart_id="+elem["heart_id"]+"&glucose_id="+elem["glucose_id"])
			elif(key=="4"):
				for elem in scheduling[key]:
					if(time.time()-elem["last_measurement"]>=480):
						r=requests.get("http://"+self.ip_others["queue_server"][0]+":"+self.ip_others["queue_server"][1]+"/retrieve?pressure_id="+elem["pressure_id"]+"&heart_id="+elem["heart_id"]+"&glucose_id="+elem["glucose_id"])
			elif(key=="5"):
				for elem in scheduling[key]:
					if(time.time()-elem["last_measurement"]>=960):
						r=requests.get("http://"+self.ip_others["queue_server"][0]+":"+self.ip_others["queue_server"][1]+"/retrieve?pressure_id="+elem["pressure_id"]+"&heart_id="+elem["heart_id"]+"&glucose_id="+elem["glucose_id"])

	
	def addToScheduling(self, data):
		data=json.loads(data)
		obj={
		"pressure_id":data["pressure_id"],
		"heart_id":data["heart_id"],
		"glucose_id":data["glucose_id"],
		"last_time":data["time_stamp"]
		}

		self.scheduling[data["code"]].append(obj)
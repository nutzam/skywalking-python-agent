import ApplicationRegisterService_pb2_grpc
import ApplicationRegisterService_pb2
import grpc
import urllib
import json




class SkyWalking(object):

	def __init__(self, agentstream=["app.danoolive.com:10800"], applicationCode="python-test-service", debug=False):
	    if isinstance(agentstream, string):
			agentstreams = [agentstreams]
		self.agentstreams = agentstreams
		self.applicationCode = applicationCode
		self.debug = debug
		self.application = None

	def update_grpc_servers(self):
		tmps = []
		for agentstream in agentstreams :
			try :
				tmp = urllib.urlopen("http://"+self.agentstream+"/agentstream/grpc").read()
				if not tmp :
					if self.debug:
						print("emtry agentstream? " + agentstream)
					continue
				grpc_servers = json.loads(tmp)
				if not grpc_servers :
					if self.debug:
						print("emtry agentstream? " + agentstream)
				tmps += grpc_servers
			except:
				if self.debug:
					print("bad agentstream="+agentstream)
		if not tmps :
			if self.debug:
				print("emtry grpc_servers")
		self.grpc_servers = tmps

	def register(self):
		for grpc_server in self.grpc_servers:
			try :
				self.channel = grpc.insecure_channel(self.grpc_servers[0])
				self.stub = ApplicationRegisterService_pb2_grpc.ApplicationRegisterServiceStub(self.channel)
				tmp = self.stub.register(ApplicationRegisterService_pb2.Application(applicationCode =[self.applicationCode]))
				if tmp and tmp.application :
					self.application = tmp.application
					break
			except:
				if self.debug:
					print("grpc_server is down? " + grpc_server)
	
sky = SkyWalking()
sky.update_grpc_servers()
sky.register()
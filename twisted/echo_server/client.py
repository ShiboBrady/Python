# -*- coding=utf-8 -*-
from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClient(protocol.Protocol):
	def sendData(self):
		data = raw_input('> ')
		if data:
			print '...sending %s...' % data
			self.transport.write(data)
		else:
			self.transport.loseConnection()	
		
	def connectionMade(self):
		self.sendData()

	def dataReceived(self, data):
		print data
		self.sendData()

class TSClientFactory(protocol.ClientFactory):
	protocol = TSClient
	clientConnentionLost = clientConnectionFailed = \
		lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClientFactory())
print '123'
reactor.run()


# -*- coding=utf-8 -*-

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServer(protocol.Protocol):
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print '...connected from : ', clnt

	def dataReceived(self, data):
		print '...send data: [%s] %s' % (ctime(), data)
		self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServer

print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()

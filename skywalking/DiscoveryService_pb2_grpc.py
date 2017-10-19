# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import DiscoveryService_pb2 as DiscoveryService__pb2
import Downstream_pb2 as Downstream__pb2


class InstanceDiscoveryServiceStub(object):
  """discovery service for application instance, this service is called when application starts
  or http client connection switch to another collector server instance
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.register = channel.unary_unary(
        '/InstanceDiscoveryService/register',
        request_serializer=DiscoveryService__pb2.ApplicationInstance.SerializeToString,
        response_deserializer=DiscoveryService__pb2.ApplicationInstanceMapping.FromString,
        )
    self.heartbeat = channel.unary_unary(
        '/InstanceDiscoveryService/heartbeat',
        request_serializer=DiscoveryService__pb2.ApplicationInstanceHeartbeat.SerializeToString,
        response_deserializer=Downstream__pb2.Downstream.FromString,
        )
    self.registerRecover = channel.unary_unary(
        '/InstanceDiscoveryService/registerRecover',
        request_serializer=DiscoveryService__pb2.ApplicationInstanceRecover.SerializeToString,
        response_deserializer=Downstream__pb2.Downstream.FromString,
        )


class InstanceDiscoveryServiceServicer(object):
  """discovery service for application instance, this service is called when application starts
  or http client connection switch to another collector server instance
  """

  def register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def heartbeat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def registerRecover(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InstanceDiscoveryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'register': grpc.unary_unary_rpc_method_handler(
          servicer.register,
          request_deserializer=DiscoveryService__pb2.ApplicationInstance.FromString,
          response_serializer=DiscoveryService__pb2.ApplicationInstanceMapping.SerializeToString,
      ),
      'heartbeat': grpc.unary_unary_rpc_method_handler(
          servicer.heartbeat,
          request_deserializer=DiscoveryService__pb2.ApplicationInstanceHeartbeat.FromString,
          response_serializer=Downstream__pb2.Downstream.SerializeToString,
      ),
      'registerRecover': grpc.unary_unary_rpc_method_handler(
          servicer.registerRecover,
          request_deserializer=DiscoveryService__pb2.ApplicationInstanceRecover.FromString,
          response_serializer=Downstream__pb2.Downstream.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'InstanceDiscoveryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ServiceNameDiscoveryServiceStub(object):
  """discovery service for ServiceName by Network address or application code
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.discovery = channel.unary_unary(
        '/ServiceNameDiscoveryService/discovery',
        request_serializer=DiscoveryService__pb2.ServiceNameCollection.SerializeToString,
        response_deserializer=DiscoveryService__pb2.ServiceNameMappingCollection.FromString,
        )


class ServiceNameDiscoveryServiceServicer(object):
  """discovery service for ServiceName by Network address or application code
  """

  def discovery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServiceNameDiscoveryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'discovery': grpc.unary_unary_rpc_method_handler(
          servicer.discovery,
          request_deserializer=DiscoveryService__pb2.ServiceNameCollection.FromString,
          response_serializer=DiscoveryService__pb2.ServiceNameMappingCollection.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ServiceNameDiscoveryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

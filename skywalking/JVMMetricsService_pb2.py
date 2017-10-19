# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JVMMetricsService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Downstream_pb2 as Downstream__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='JVMMetricsService.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x17JVMMetricsService.proto\x1a\x10\x44ownstream.proto\"H\n\nJVMMetrics\x12\x1b\n\x07metrics\x18\x01 \x03(\x0b\x32\n.JVMMetric\x12\x1d\n\x15\x61pplicationInstanceId\x18\x02 \x01(\x05\"w\n\tJVMMetric\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x11\n\x03\x63pu\x18\x02 \x01(\x0b\x32\x04.CPU\x12\x17\n\x06memory\x18\x03 \x03(\x0b\x32\x07.Memory\x12\x1f\n\nmemoryPool\x18\x04 \x03(\x0b\x32\x0b.MemoryPool\x12\x0f\n\x02gc\x18\x05 \x03(\x0b\x32\x03.GC\"\x1b\n\x03\x43PU\x12\x14\n\x0cusagePercent\x18\x02 \x01(\x01\"T\n\x06Memory\x12\x0e\n\x06isHeap\x18\x01 \x01(\x08\x12\x0c\n\x04init\x18\x02 \x01(\x03\x12\x0b\n\x03max\x18\x03 \x01(\x03\x12\x0c\n\x04used\x18\x04 \x01(\x03\x12\x11\n\tcommitted\x18\x05 \x01(\x03\"`\n\nMemoryPool\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.PoolType\x12\x0c\n\x04init\x18\x02 \x01(\x03\x12\x0b\n\x03max\x18\x03 \x01(\x03\x12\x0c\n\x04used\x18\x04 \x01(\x03\x12\x10\n\x08\x63ommited\x18\x05 \x01(\x03\"<\n\x02GC\x12\x19\n\x06phrase\x18\x01 \x01(\x0e\x32\t.GCPhrase\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x0c\n\x04time\x18\x03 \x01(\x03*\x80\x01\n\x08PoolType\x12\x14\n\x10\x43ODE_CACHE_USAGE\x10\x00\x12\x10\n\x0cNEWGEN_USAGE\x10\x01\x12\x10\n\x0cOLDGEN_USAGE\x10\x02\x12\x12\n\x0eSURVIVOR_USAGE\x10\x03\x12\x11\n\rPERMGEN_USAGE\x10\x04\x12\x13\n\x0fMETASPACE_USAGE\x10\x05*\x1c\n\x08GCPhrase\x12\x07\n\x03NEW\x10\x00\x12\x07\n\x03OLD\x10\x01\x32:\n\x11JVMMetricsService\x12%\n\x07\x63ollect\x12\x0b.JVMMetrics\x1a\x0b.Downstream\"\x00\x42$\n org.skywalking.apm.network.protoP\x01\x62\x06proto3')
  ,
  dependencies=[Downstream__pb2.DESCRIPTOR,])

_POOLTYPE = _descriptor.EnumDescriptor(
  name='PoolType',
  full_name='PoolType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CODE_CACHE_USAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEWGEN_USAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OLDGEN_USAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SURVIVOR_USAGE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMGEN_USAGE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METASPACE_USAGE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=516,
  serialized_end=644,
)
_sym_db.RegisterEnumDescriptor(_POOLTYPE)

PoolType = enum_type_wrapper.EnumTypeWrapper(_POOLTYPE)
_GCPHRASE = _descriptor.EnumDescriptor(
  name='GCPhrase',
  full_name='GCPhrase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OLD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=646,
  serialized_end=674,
)
_sym_db.RegisterEnumDescriptor(_GCPHRASE)

GCPhrase = enum_type_wrapper.EnumTypeWrapper(_GCPHRASE)
CODE_CACHE_USAGE = 0
NEWGEN_USAGE = 1
OLDGEN_USAGE = 2
SURVIVOR_USAGE = 3
PERMGEN_USAGE = 4
METASPACE_USAGE = 5
NEW = 0
OLD = 1



_JVMMETRICS = _descriptor.Descriptor(
  name='JVMMetrics',
  full_name='JVMMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='JVMMetrics.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicationInstanceId', full_name='JVMMetrics.applicationInstanceId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=117,
)


_JVMMETRIC = _descriptor.Descriptor(
  name='JVMMetric',
  full_name='JVMMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='JVMMetric.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu', full_name='JVMMetric.cpu', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='JVMMetric.memory', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memoryPool', full_name='JVMMetric.memoryPool', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gc', full_name='JVMMetric.gc', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=238,
)


_CPU = _descriptor.Descriptor(
  name='CPU',
  full_name='CPU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='usagePercent', full_name='CPU.usagePercent', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=267,
)


_MEMORY = _descriptor.Descriptor(
  name='Memory',
  full_name='Memory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isHeap', full_name='Memory.isHeap', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init', full_name='Memory.init', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='Memory.max', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='Memory.used', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='committed', full_name='Memory.committed', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=353,
)


_MEMORYPOOL = _descriptor.Descriptor(
  name='MemoryPool',
  full_name='MemoryPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='MemoryPool.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init', full_name='MemoryPool.init', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='MemoryPool.max', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='MemoryPool.used', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commited', full_name='MemoryPool.commited', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=451,
)


_GC = _descriptor.Descriptor(
  name='GC',
  full_name='GC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phrase', full_name='GC.phrase', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='GC.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='GC.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=513,
)

_JVMMETRICS.fields_by_name['metrics'].message_type = _JVMMETRIC
_JVMMETRIC.fields_by_name['cpu'].message_type = _CPU
_JVMMETRIC.fields_by_name['memory'].message_type = _MEMORY
_JVMMETRIC.fields_by_name['memoryPool'].message_type = _MEMORYPOOL
_JVMMETRIC.fields_by_name['gc'].message_type = _GC
_MEMORYPOOL.fields_by_name['type'].enum_type = _POOLTYPE
_GC.fields_by_name['phrase'].enum_type = _GCPHRASE
DESCRIPTOR.message_types_by_name['JVMMetrics'] = _JVMMETRICS
DESCRIPTOR.message_types_by_name['JVMMetric'] = _JVMMETRIC
DESCRIPTOR.message_types_by_name['CPU'] = _CPU
DESCRIPTOR.message_types_by_name['Memory'] = _MEMORY
DESCRIPTOR.message_types_by_name['MemoryPool'] = _MEMORYPOOL
DESCRIPTOR.message_types_by_name['GC'] = _GC
DESCRIPTOR.enum_types_by_name['PoolType'] = _POOLTYPE
DESCRIPTOR.enum_types_by_name['GCPhrase'] = _GCPHRASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JVMMetrics = _reflection.GeneratedProtocolMessageType('JVMMetrics', (_message.Message,), dict(
  DESCRIPTOR = _JVMMETRICS,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:JVMMetrics)
  ))
_sym_db.RegisterMessage(JVMMetrics)

JVMMetric = _reflection.GeneratedProtocolMessageType('JVMMetric', (_message.Message,), dict(
  DESCRIPTOR = _JVMMETRIC,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:JVMMetric)
  ))
_sym_db.RegisterMessage(JVMMetric)

CPU = _reflection.GeneratedProtocolMessageType('CPU', (_message.Message,), dict(
  DESCRIPTOR = _CPU,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:CPU)
  ))
_sym_db.RegisterMessage(CPU)

Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), dict(
  DESCRIPTOR = _MEMORY,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:Memory)
  ))
_sym_db.RegisterMessage(Memory)

MemoryPool = _reflection.GeneratedProtocolMessageType('MemoryPool', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYPOOL,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:MemoryPool)
  ))
_sym_db.RegisterMessage(MemoryPool)

GC = _reflection.GeneratedProtocolMessageType('GC', (_message.Message,), dict(
  DESCRIPTOR = _GC,
  __module__ = 'JVMMetricsService_pb2'
  # @@protoc_insertion_point(class_scope:GC)
  ))
_sym_db.RegisterMessage(GC)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n org.skywalking.apm.network.protoP\001'))

_JVMMETRICSSERVICE = _descriptor.ServiceDescriptor(
  name='JVMMetricsService',
  full_name='JVMMetricsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=676,
  serialized_end=734,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='JVMMetricsService.collect',
    index=0,
    containing_service=None,
    input_type=_JVMMETRICS,
    output_type=Downstream__pb2._DOWNSTREAM,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JVMMETRICSSERVICE)

DESCRIPTOR.services_by_name['JVMMetricsService'] = _JVMMETRICSSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class JVMMetricsServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.collect = channel.unary_unary(
          '/JVMMetricsService/collect',
          request_serializer=JVMMetrics.SerializeToString,
          response_deserializer=Downstream__pb2.Downstream.FromString,
          )


  class JVMMetricsServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def collect(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_JVMMetricsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'collect': grpc.unary_unary_rpc_method_handler(
            servicer.collect,
            request_deserializer=JVMMetrics.FromString,
            response_serializer=Downstream__pb2.Downstream.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'JVMMetricsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaJVMMetricsServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def collect(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaJVMMetricsServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def collect(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    collect.future = None


  def beta_create_JVMMetricsService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('JVMMetricsService', 'collect'): JVMMetrics.FromString,
    }
    response_serializers = {
      ('JVMMetricsService', 'collect'): Downstream__pb2.Downstream.SerializeToString,
    }
    method_implementations = {
      ('JVMMetricsService', 'collect'): face_utilities.unary_unary_inline(servicer.collect),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_JVMMetricsService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('JVMMetricsService', 'collect'): JVMMetrics.SerializeToString,
    }
    response_deserializers = {
      ('JVMMetricsService', 'collect'): Downstream__pb2.Downstream.FromString,
    }
    cardinalities = {
      'collect': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'JVMMetricsService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: player.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cplayer.proto\"{\n\x06Player\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x08position\x18\x03 \x01(\x0b\x32\t.Position\x12\x17\n\x06\x61rrows\x18\x04 \x01(\x0b\x32\x07.Arrows\x12\x10\n\x08rotation\x18\x05 \x01(\x02\x12\x0f\n\x07\x61nim_id\x18\x06 \x01(\x05\" \n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"!\n\tDirection\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"#\n\x07Players\x12\x18\n\x07players\x18\x01 \x03(\x0b\x32\x07.Player\"R\n\x05\x41rrow\x12\x1b\n\x08position\x18\x01 \x01(\x0b\x32\t.Position\x12\x1d\n\tdirection\x18\x02 \x01(\x0b\x32\n.Direction\x12\r\n\x05speed\x18\x03 \x01(\x05\" \n\x06\x41rrows\x12\x16\n\x06\x61rrows\x18\x01 \x03(\x0b\x32\x06.Arrowb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'player_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYER._serialized_start=16
  _PLAYER._serialized_end=139
  _POSITION._serialized_start=141
  _POSITION._serialized_end=173
  _DIRECTION._serialized_start=175
  _DIRECTION._serialized_end=208
  _PLAYERS._serialized_start=210
  _PLAYERS._serialized_end=245
  _ARROW._serialized_start=247
  _ARROW._serialized_end=329
  _ARROWS._serialized_start=331
  _ARROWS._serialized_end=363
# @@protoc_insertion_point(module_scope)

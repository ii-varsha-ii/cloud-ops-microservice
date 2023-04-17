# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tvpc.proto\"E\n\x13RegionAndVpcRequest\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x13\n\x06vpc_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_vpc_id\"\x1f\n\nListOfVpcs\x12\x11\n\x03vpc\x18\x01 \x03(\x0b\x32\x04.Vpc\")\n\rListOfSubnets\x12\x18\n\x07subnets\x18\x01 \x03(\x0b\x32\x07.Subnet\"]\n\x03Vpc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncidr_block\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x18\n\x07subnets\x18\x05 \x03(\x0b\x32\x07.Subnet\"y\n\x06Subnet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x03 \x01(\t\x12\x12\n\ncidr_block\x18\x04 \x01(\t\x12\x0e\n\x06vpc_id\x18\x05 \x01(\t\x12\x16\n\x0eroute_table_id\x18\x06 \x01(\t\"h\n\x10\x43reateVpcRequest\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07ip_cidr\x18\x03 \x01(\t\x12%\n\x07subnets\x18\x04 \x03(\x0b\x32\x14.CreateSubnetRequest\"\x82\x01\n\x13\x43reateSubnetRequest\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x61vailability_zone\x18\x03 \x01(\t\x12\x12\n\ncidr_block\x18\x04 \x01(\t\x12\x0e\n\x06vpc_id\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x06 \x01(\t2\xdf\x01\n\nVpcService\x12/\n\x14\x43reateVpcWithSubnets\x12\x11.CreateVpcRequest\x1a\x04.Vpc\x12\x38\n\x13GetVpcBasedOnRegion\x12\x14.RegionAndVpcRequest\x1a\x0b.ListOfVpcs\x12\x37\n\x0fGetSubnetsInVpc\x12\x14.RegionAndVpcRequest\x1a\x0e.ListOfSubnets\x12-\n\x0c\x43reateSubnet\x12\x14.CreateSubnetRequest\x1a\x07.Subnetb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGIONANDVPCREQUEST._serialized_start=13
  _REGIONANDVPCREQUEST._serialized_end=82
  _LISTOFVPCS._serialized_start=84
  _LISTOFVPCS._serialized_end=115
  _LISTOFSUBNETS._serialized_start=117
  _LISTOFSUBNETS._serialized_end=158
  _VPC._serialized_start=160
  _VPC._serialized_end=253
  _SUBNET._serialized_start=255
  _SUBNET._serialized_end=376
  _CREATEVPCREQUEST._serialized_start=378
  _CREATEVPCREQUEST._serialized_end=482
  _CREATESUBNETREQUEST._serialized_start=485
  _CREATESUBNETREQUEST._serialized_end=615
  _VPCSERVICE._serialized_start=618
  _VPCSERVICE._serialized_end=841
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: organization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12organization.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"|\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x61rn\x18\x02 \x01(\t\x12\x1a\n\x12master_account_arn\x18\x03 \x01(\t\x12\x19\n\x11master_account_id\x18\x04 \x01(\t\x12\x1c\n\x14master_account_email\x18\x05 \x01(\t\"\x80\x01\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x61rn\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x15\n\rjoined_method\x18\x06 \x01(\t\x12\x18\n\x10joined_timestamp\x18\x07 \x01(\t\",\n\x0eListOfAccounts\x12\x1a\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x08.Account\"\x1f\n\tAccountId\x12\x12\n\naccount_id\x18\x01 \x01(\t\"b\n\x14InviteAccountRequest\x12\x17\n\naccount_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x65mail_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\r\n\x0b_account_idB\x0b\n\t_email_id\" \n\x04Pair\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x0c\n\x04Type\x18\x02 \x01(\t\"\xa2\x01\n\x15InviteAccountResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x61rn\x18\x02 \x01(\t\x12\x16\n\x07parties\x18\x03 \x03(\x0b\x32\x05.Pair\x12\r\n\x05state\x18\x04 \x01(\t\x12\x1b\n\x13requested_timestamp\x18\x05 \x01(\t\x12\x1c\n\x14\x65xpiration_timestamp\x18\x06 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x07 \x01(\t2\xa6\x02\n\x13OrganizationService\x12:\n\x0fGetOrganization\x12\x16.google.protobuf.Empty\x1a\r.Organization\"\x00\x12\x46\n\x19GetAccountsInOrganization\x12\x16.google.protobuf.Empty\x1a\x0f.ListOfAccounts\"\x00\x12;\n!GetAccountInOrganizationBasedOnId\x12\n.AccountId\x1a\x08.Account\"\x00\x12N\n\x1bInviteAccountToOrganization\x12\x15.InviteAccountRequest\x1a\x16.InviteAccountResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'organization_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORGANIZATION._serialized_start=84
  _ORGANIZATION._serialized_end=208
  _ACCOUNT._serialized_start=211
  _ACCOUNT._serialized_end=339
  _LISTOFACCOUNTS._serialized_start=341
  _LISTOFACCOUNTS._serialized_end=385
  _ACCOUNTID._serialized_start=387
  _ACCOUNTID._serialized_end=418
  _INVITEACCOUNTREQUEST._serialized_start=420
  _INVITEACCOUNTREQUEST._serialized_end=518
  _PAIR._serialized_start=520
  _PAIR._serialized_end=552
  _INVITEACCOUNTRESPONSE._serialized_start=555
  _INVITEACCOUNTRESPONSE._serialized_end=717
  _ORGANIZATIONSERVICE._serialized_start=720
  _ORGANIZATIONSERVICE._serialized_end=1014
# @@protoc_insertion_point(module_scope)
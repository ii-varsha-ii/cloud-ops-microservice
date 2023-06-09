# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import organization_pb2 as organization__pb2


class OrganizationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrganization = channel.unary_unary(
                '/OrganizationService/GetOrganization',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=organization__pb2.Organization.FromString,
                )
        self.GetAccountsInOrganization = channel.unary_unary(
                '/OrganizationService/GetAccountsInOrganization',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=organization__pb2.ListOfAccounts.FromString,
                )
        self.GetAccountInOrganizationBasedOnId = channel.unary_unary(
                '/OrganizationService/GetAccountInOrganizationBasedOnId',
                request_serializer=organization__pb2.AccountId.SerializeToString,
                response_deserializer=organization__pb2.Account.FromString,
                )
        self.InviteAccountToOrganization = channel.unary_unary(
                '/OrganizationService/InviteAccountToOrganization',
                request_serializer=organization__pb2.InviteAccountRequest.SerializeToString,
                response_deserializer=organization__pb2.InviteAccountResponse.FromString,
                )


class OrganizationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountsInOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountInOrganizationBasedOnId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InviteAccountToOrganization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganization,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=organization__pb2.Organization.SerializeToString,
            ),
            'GetAccountsInOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountsInOrganization,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=organization__pb2.ListOfAccounts.SerializeToString,
            ),
            'GetAccountInOrganizationBasedOnId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountInOrganizationBasedOnId,
                    request_deserializer=organization__pb2.AccountId.FromString,
                    response_serializer=organization__pb2.Account.SerializeToString,
            ),
            'InviteAccountToOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.InviteAccountToOrganization,
                    request_deserializer=organization__pb2.InviteAccountRequest.FromString,
                    response_serializer=organization__pb2.InviteAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OrganizationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrganizationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrganizationService/GetOrganization',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            organization__pb2.Organization.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccountsInOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrganizationService/GetAccountsInOrganization',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            organization__pb2.ListOfAccounts.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccountInOrganizationBasedOnId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrganizationService/GetAccountInOrganizationBasedOnId',
            organization__pb2.AccountId.SerializeToString,
            organization__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InviteAccountToOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrganizationService/InviteAccountToOrganization',
            organization__pb2.InviteAccountRequest.SerializeToString,
            organization__pb2.InviteAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

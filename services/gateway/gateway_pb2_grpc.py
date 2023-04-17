# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gateway_pb2 as gateway__pb2


class GatewayServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransitGateway = channel.unary_unary(
                '/GatewayService/GetTransitGateway',
                request_serializer=gateway__pb2.RegionRequest.SerializeToString,
                response_deserializer=gateway__pb2.TransitGateway.FromString,
                )


class GatewayServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTransitGateway(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransitGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransitGateway,
                    request_deserializer=gateway__pb2.RegionRequest.FromString,
                    response_serializer=gateway__pb2.TransitGateway.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GatewayService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTransitGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GatewayService/GetTransitGateway',
            gateway__pb2.RegionRequest.SerializeToString,
            gateway__pb2.TransitGateway.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

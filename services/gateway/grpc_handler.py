from concurrent import futures

import grpc

from services.gateway import gateway_pb2_grpc
from services.gateway.gateway_pb2 import TransitGateway
from services.gateway.gateway_pb2_grpc import GatewayServiceServicer
from services.gateway.transit_gateway import check_if_tgw_exists


class GatewayService(GatewayServiceServicer):
    def GetTransitGateway(self, request, context):
        response = check_if_tgw_exists(request.region)
        print(response)
        if response:
            return TransitGateway(
                id=response.Id,
                arn=response.Arn,
                state=response.State,
                owner_id=response.OwnerId,
                creation_time=str(response.CreationTime),
                description=response.Description
            )
        else:
            return TransitGateway()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gateway_pb2_grpc.add_GatewayServiceServicer_to_server(
        GatewayService(), server
    )
    server.add_insecure_port('[::]:50053')
    print("Server started at port 50053")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

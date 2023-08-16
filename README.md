# Manage AWS cloud operations ( in progress )

This project comprises of AWS cloud operations that can be used to create and manage AWS services. 

## Developer guide:
Designed in a microservice architecture fashion comes along with gRPC protos to run it as a seperate service. Run the Makefile to generate the protos 

**Language:** Python   
**Framework:** Boto3

## Makefile:
gateway:
`python -m grpc_tools.protoc --python_out=./services/gateway/ --pyi_out=./services/gateway/ --grpc_python_out=./services/gateway/ --proto_path protos/ gateway.proto`
	
organizations:
`python -m grpc_tools.protoc --python_out=./services/organization/ --pyi_out=./services/organization/ --grpc_python_out=./services/organization/ --proto_path protos/ protos/organization.proto`

vpc:
`python -m grpc_tools.protoc --python_out=./services/vpc/ --pyi_out=./services/vpc/ --grpc_python_out=./services/vpc/ --proto_path protos/ protos/vpc.proto`


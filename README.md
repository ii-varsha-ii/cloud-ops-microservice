organizations:
`python -m grpc_tools.protoc --python_out=./services/organization/ --pyi_out=./services/organization/ --grpc_python_out=./services/organization/ --proto_path protos/ protos/organization.proto`

vpc:
`python -m grpc_tools.protoc --python_out=./services/vpc/ --pyi_out=./services/vpc/ --grpc_python_out=./services/vpc/ --proto_path protos/ protos/vpc.proto`


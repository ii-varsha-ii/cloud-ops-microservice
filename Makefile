generate-protos:
	@echo "Generating Proto..."
	python -m grpc_tools.protoc --python_out=./services/organization/ --pyi_out=./services/organization/ --grpc_python_out=./services/organization/ --proto_path protos/ organization.proto
	python -m grpc_tools.protoc --python_out=./services/vpc/ --pyi_out=./services/vpc/ --grpc_python_out=./services/vpc/ --proto_path protos/ vpc.proto
	python -m grpc_tools.protoc --python_out=./services/gateway/ --pyi_out=./services/gateway/ --grpc_python_out=./services/gateway/ --proto_path protos/ gateway.proto
	@echo "Generated pb files"


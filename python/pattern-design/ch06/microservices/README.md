# Microservices with gRPC

This project demonstrates microservices architecture using gRPC for inter-service communication.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .venv/                 # Virtual environment
└── grpc/
    ├── payment.proto      # Protocol buffer definition
    ├── payment_pb2.py     # Generated message classes
    ├── payment_pb2_grpc.py # Generated gRPC service stubs
    ├── payment_service.py # Payment service implementation
    └── client.py          # Client implementation
```

## Setup

1. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## gRPC Code Generation

To generate Python code from the Protocol Buffer definitions, run the following command from the project root:

```bash
source .venv/bin/activate && cd grpc && python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. payment.proto
```

This command will:

- Activate the virtual environment
- Navigate to the `grpc` directory
- Generate `payment_pb2.py` (message classes)
- Generate `payment_pb2_grpc.py` (service stubs)

### Command Breakdown

- `python -m grpc_tools.protoc`: Run the Protocol Buffer compiler
- `-I.`: Include current directory for imports
- `--python_out=.`: Output Python message classes to current directory
- `--grpc_python_out=.`: Output gRPC service stubs to current directory
- `payment.proto`: Source Protocol Buffer file

## Services

### Payment Service

The payment service is defined in `payment.proto` and provides:

- **ProcessPayment**: Handles payment processing requests

**Request Message (`PaymentRequest`):**

- `order_id`: Unique order identifier
- `amount`: Payment amount
- `currency`: Currency code
- `user_id`: User identifier

**Response Message (`PaymentResponse`):**

- `payment_id`: Generated payment identifier
- `status`: Payment status ("SUCCESS", "FAILED", etc.)

## Running the Services

### Start the Payment Service

1. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

2. **Navigate to the grpc directory and start the service:**

   ```bash
   cd grpc
   # python3 payment_service.py
   ```

   You should see:

   ```
   Payment Processing Service ready!
   ```

   The service will be running on `[::]:50051` (all interfaces, port 50051).

### Run the Client

In another terminal, you can run the client to test the service:

```bash
source .venv/bin/activate
cd grpc
# python3 client.py
```

You should see:

```
Payment Service responded.
Response status: SUCCESS
```

## Development Notes

- Always regenerate the Python files after modifying the `.proto` file
- The generated files should not be manually edited
- Use the virtual environment to ensure consistent dependencies

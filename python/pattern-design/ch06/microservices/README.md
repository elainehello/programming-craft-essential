# Microservices with gRPC and LLM Integration

This project demonstrates microservices architecture using gRPC for inter-service communication and includes an LLM service using Lanarky for AI-powered chat functionality.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env                   # Environment variables (OpenAI API key)
├── .venv/                 # Virtual environment
├── grpc/                  # gRPC Payment Service
│   ├── payment.proto      # Protocol buffer definition
│   ├── payment_pb2.py     # Generated message classes
│   ├── payment_pb2_grpc.py # Generated gRPC service stubs
│   ├── payment_service.py # Payment service implementation
│   ├── client.py          # Payment client implementation
│   └── note.txt
└── lanarky/               # LLM Service with Lanarky
    ├── llm_service.py     # FastAPI LLM service
    └── client.py          # LLM client implementation
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

3. **Configure environment variables:**

   Create a `.env` file in the project root with your OpenAI API key:

   ```bash
   echo "OPENAI_API_KEY=your_actual_openai_api_key_here" > .env
   ```

## Services

### Payment Service (gRPC)

The payment service is defined in [`payment.proto`](grpc/payment.proto) and provides:

- **ProcessPayment**: Handles payment processing requests using gRPC

**Request Message (`PaymentRequest`):**

- `order_id`: Unique order identifier
- `amount`: Payment amount
- `currency`: Currency code
- `user_id`: User identifier

**Response Message (`PaymentResponse`):**

- `payment_id`: Generated payment identifier
- `status`: Payment status ("SUCCESS", "FAILED", etc.)

### LLM Service (FastAPI + Lanarky)

The LLM service provides AI-powered chat functionality using:

- **FastAPI** for HTTP REST API
- **Lanarky** framework for OpenAI integration
- **Streaming responses** for real-time chat

**Endpoint:**

- `POST /chat`: Processes chat messages and returns AI responses

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

## Running the Services

### Start the Payment Service (gRPC)

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

### Run the Payment Client

In another terminal, you can run the client to test the payment service:

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

### Start the LLM Service (FastAPI)

1. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

2. **Navigate to the lanarky directory and start the service:**

   ```bash
   cd lanarky
   # python3 llm_service.py
   ```

   You should see:

   ```
   INFO:     Started server process [PID]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

   The LLM service will be running on `http://127.0.0.1:8000`.

### Run the LLM Client

In another terminal, you can test the LLM service:

```bash
source .venv/bin/activate
cd lanarky
# python3 client.py "Hello, how are you?"
```

You should see streaming responses from the AI:

```
message: Hello! I'm doing well, thank you for asking...
```

## API Endpoints

### Payment Service (gRPC - Port 50051)

- `ProcessPayment`: gRPC method for payment processing

### LLM Service (HTTP - Port 8000)

- `POST /chat`: Chat with AI assistant
  - Parameters: `stream=true/false`
  - Body: `{"messages": [{"role": "user", "content": "your message"}]}`

## Environment Variables

The project uses the following environment variables (stored in `.env`):

- `OPENAI_API_KEY`: Your OpenAI API key for LLM functionality

## Dependencies

Key dependencies include:

- `grpcio`: Core gRPC library
- `grpcio-tools`: Protocol buffer compiler tools
- `protobuf`: Protocol buffer runtime
- `fastapi`: Modern web framework for APIs
- `lanarky`: Framework for LLM integration
- `uvicorn`: ASGI server for FastAPI
- `openai`: OpenAI Python client
- `python-dotenv`: Environment variable management

## Development Notes

- Always regenerate the Python files after modifying the `.proto` file
- The generated files should not be manually edited
- Use the virtual environment to ensure consistent dependencies
- Keep your OpenAI API key secure and never commit it to version control
- The `.env` file is already added to `.gitignore` for security
- Ensure you have sufficient OpenAI API credits for the LLM service to function

## Architecture

This microservices setup demonstrates:

1. **gRPC Communication**: Efficient binary protocol for internal service communication
2. **REST API**: Standard HTTP interface for external clients
3. **AI Integration**: LLM capabilities for intelligent responses
4. **Environment Configuration**: Secure management of API keys and settings
5. **Multiple Protocols**: Both gRPC and HTTP services in the same project

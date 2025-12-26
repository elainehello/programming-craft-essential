import click
import sys
from lanarky.clients import StreamingClient

args = sys.argv[1:]
if len(args) == 1:
    message = args[0]

    # Specify the base URL where the service is running
    client = StreamingClient(base_url="http://127.0.0.1:8000")
    for event in client.stream_response(
        "POST",
        "/chat",
        params={"stream": "false"},
        json={"messages": [dict(role="user", content=message)]},
    ):
        print(f"{event.event}: {event.data}")
else:
    print("You need to pass a message!")

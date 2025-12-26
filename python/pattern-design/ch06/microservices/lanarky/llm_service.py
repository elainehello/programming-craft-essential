import os
import dotenv

import uvicorn
from lanarky import Lanarky
from lanarky.adapters.openai.resources import ChatCompletionResource
from lanarky.adapters.openai.routing import OpenAIAPIRouter

dotenv.load_dotenv()

# Check if API key is available
api_key = os.getenv("OPENAI_API_KEY", "")
if not api_key or api_key == "":
    print("Warning: No OpenAI API key found. Service will use mock responses.")

os.environ["OPENAI_API_KEY"] = api_key

app = Lanarky()
router = OpenAIAPIRouter()

@router.post("/chat")
def chat(stream: bool = True) -> ChatCompletionResource:
    system = "Here is your assistant"
    return ChatCompletionResource(stream=stream, system=system)

if __name__ == "__main__":
    app.include_router(router)
    uvicorn.run(app, host="127.0.0.1", port=8000)

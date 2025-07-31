from ayeto import AyetoClient
from ayeto.types import LLMMessage
from ayeto.requests import ChatRequest


# Initialize the Ayeto client
client = AyetoClient()

# Create a message
message = LLMMessage(
    role="user",
    content="Explain quantum computing in simple terms"
)

# Create chat request
chat_request = ChatRequest(
    model="gpt-4.1",
    message=message,
    max_tokens=500,
    relevant_history=True,
    dynamic_tools=True
)

# Send chat request
response = client.chat(chat_request)
print(response.content)
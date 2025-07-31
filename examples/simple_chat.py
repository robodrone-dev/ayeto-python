from ayeto import AyetoClient

# Initialize with API key from environment variable AYETO_API_KEY
client = AyetoClient()

# Send a simple chat request
response = client.simple_chat(
    model_id="gpt-4.1-nano",
    prompt="What is the capital of Czech Republic?"
)

# Print the response from the AI model
print(response.response)
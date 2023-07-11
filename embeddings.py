import openai
from apikey import OPENAI_API_KEY
from embed_this import text

openai.api_key = OPENAI_API_KEY
embeds = openai.Embedding.create(
  model="text-embedding-ada-002",
  input=text
)

print(embeds)

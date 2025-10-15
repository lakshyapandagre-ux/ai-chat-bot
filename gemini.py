import google.genai as genai
client = genai.Client(api_key="AIzaSyCYgdVUyo5tjIcCcw0mQDSVC3f7VRZpM2k")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello Gemini, are you working?"
)
print(response.output_text)

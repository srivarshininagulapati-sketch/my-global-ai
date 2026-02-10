from google import genai

client = genai.Client(
    api_key="AIzaSyC2wD2DtgZVqEHPLyHme4wSjlvHfG9EWSQ"
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello Gemini, nuvvu work avtunnava?"
)

print(response.text)


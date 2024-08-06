from openai import OpenAI
client = OpenAI()

def getResponse(query):

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": """You are an excellent programmer, expert in developing web applications. 
            You will be given following pieces instructions. Your task is to generate an index.html file that satisfies that instructions.
            Just generate index.html file. No explanation needed.
            """},
        {"role": "user", "content": query}
    ]
    )

    response  = completion.choices[0].message.content
    return response

if __name__ == "__main__":
    print(getResponse("generate a simple fashion website?"))
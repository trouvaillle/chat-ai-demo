from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
while True:
    prompt = input("You: ")
    output = model.generate(prompt, max_tokens=3000)
    print(output)

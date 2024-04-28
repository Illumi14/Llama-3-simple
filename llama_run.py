import ollama

def again():
    print("\n")
    input_question = input("enter a question (or press e to exit): ")
    if input_question == "e":
        exit
    else:
        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': input_question}],
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        again()

again()
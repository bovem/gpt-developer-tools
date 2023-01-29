import openai

def send_gpt_request(script_paths, line_start, line_end, prompt, open_ai_api_key, model_engine, max_tokens, n, temperature):
    for script_path in script_paths:
        with open(script_path, "r") as script:
            print("\nInput Script: {}".format(script_path))
            print()

            openai.api_key = open_ai_api_key

            prompt+="\n "
            line_start = line_start if type(line_start)==int else line_start[0]
            total_lines = sum(1 for line in script)
            line_end = total_lines if line_end[0]==None else line_end[0]

            script.seek(0)

            for i, line in enumerate(script):
                if line_start<=(i+1) and line_end>=(i+1):
                    prompt+=line
                elif line_end<(i+1):
                    break

            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens,
                n=n,
                stop=None,
                temperature=temperature,
            )

            response = completion.choices[0].text
            print("ChatGPT's Response:")
            print(response)
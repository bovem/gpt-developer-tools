# GPT CLI Debugger

A CLI utility that could be used for debugging or fetching an explaination of a script.

## Testing and Installation
1. Create virtual environment.
```bash
python3 -m virtualenv venv
```

2. Activate virtual environment.
```bash
source venv/bin/activate
```

3. Install CLI utility `gcd`
```bash
python3 -m pip install --editable .
```

4. Add your OpenAI API key as environment variable. You can generate one from [beta.openai.com](https://beta.openai.com/account/api-keys) if you already have an OpenAI account.
```bash
export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

5. Run `gcd` utility with target script passed as path
```bash
gcd explain --path ./gpt_cli_debugger.py 
```

## Sample Output
```bash
Input Script: ./gpt_cli_debugger.py

ChatGPT's Response:


if __name__ == '__main__':
    cli()

This script is used to debug or explain a script using ChatGPT. The script uses the click library to create a command line interface and import the requester and utils modules from the src package. The cli() function is used to create the command line group. The debug() and explain() functions are used to debug or explain a script respectively. Both functions take in the path to the script, the starting and ending line of the script, the model engine, max tokens, number of outputs, temperature and prompt message to be used by ChatGPT. The open_ai_api_key is retrieved from the environment variable OPENAI_API_KEY and is used to send the request to ChatGPT. Finally, the cli() function is called to execute the command line interface.
```
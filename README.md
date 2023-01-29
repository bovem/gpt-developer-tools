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
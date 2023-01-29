# GPT Developer Tools

A CLI utility based on OpenAI's [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) that helps developers in:
* Debugging
* Explaning/Documenting an undocumented script
* Creating new scripts based on prompt

## Installation
### Prerequisites
1. `python3` and `python3-pip` packages should be installed.
2. OpenAI API Key. You can generate one by visiting [beta.openai.com](https://beta.openai.com/account/api-keys)

### Local Installation
1. Install `gpt-developer-tools` PyPI package using `pip`.
```bash
python3 -m pip install gpt-developer-tools
```

2. Export `OPENAI_API_KEY` environment variable.
```bash
export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

3. Run `gdt` command with arguments and options.
```bash
gdt explain --path ./gpt_developer_tools.py 
```

## Usage
* To debug a script with `gdt`
```bash
gdt debug --path ./setup.py
```

* To debug first 7 lines of a script
```bash
gdt debug --path ./setup.py --line-end 7
```

* To debug specific lines of a script
```bash
gdt debug --path ./setup.py --line-start 7 --line-end 17
```

* To debug a script with a different prompt
```bash
gdt debug --path ./setup.py --line-start 7 --line-end 17 --prompt-message "Debug this script"
```

* To fetch an explanation/documentation for a script
```bash
gdt explain --path ./setup.py --line-start 7 --line-end 17 --prompt-message "Explain this script to me line by line"
```

* To create and save a script
```bash
gdt create -pm "Write a merge sort program in Java" -w --path ./sorting.java
```

## Sample Output
```bash
Input Script: ./gpt_developer_tools.py

ChatGPT's Response:


if __name__ == '__main__':
    cli()

This script is used to debug or explain a script using ChatGPT. The script uses the click library 
to create a command line interface and import the requester and utils modules from the src package. 
The cli() function is used to create the command line group. The debug() and explain() functions are 
used to debug or explain a script respectively. Both functions take in the path to the script, the 
starting and ending line of the script, the model engine, max tokens, number of outputs, temperature 
and prompt message to be used by ChatGPT. The open_ai_api_key is retrieved from the environment 
variable OPENAI_API_KEY and is used to send the request to ChatGPT. Finally, the cli() function is 
called to execute the command line interface.
```

## Development and Testing
1. Create virtual environment.
```bash
python3 -m virtualenv venv
```

2. Activate virtual environment.
```bash
source venv/bin/activate
```

3. Install CLI utility `gdt`
```bash
python3 -m pip install --editable .
```

4. Add your OpenAI API key as environment variable. You can generate one from [beta.openai.com](https://beta.openai.com/account/api-keys) if you already have an OpenAI account.
```bash
export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

5. Run `gdt` utility with target script passed as path
```bash
gdt explain --path ./gpt_developer_tools.py 
```

Follow OpenAI's [API Documentation](https://beta.openai.com/docs/api-reference/completions/create) for details related to models and predictions.
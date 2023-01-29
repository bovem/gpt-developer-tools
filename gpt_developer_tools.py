import click
from src import requester, utils
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--path', type=utils.file_path, help='Path to the script')
@click.option('-ls', '--line-start', type=int, help='Starting line of the script', default=1)
@click.option('-le', '--line-end', type=int, help='Ending line of the script', default=None)
@click.option('-me', '--model-engine', type=str, help='Model Engine to be used by ChatGPT', default="text-davinci-003")
@click.option('-mt', '--max-tokens', type=int, help='Max tokens to be used by ChatGPT', default=1024)
@click.option('-n', '--number-of-outputs', type=int, help='Number of outputs by ChatGPT', default=1)
@click.option('-t', '--temperature', type=float, help='Temperature of the model by ChatGPT', default=0.5)
@click.option('-pm', '--prompt-message', type=str, help='Prompt message for ChatGPT', default='Can you debug this script for me')
def debug(path, line_start, line_end, model_engine, max_tokens, number_of_outputs, temperature, prompt_message):
    open_ai_api_key = os.environ.get("OPENAI_API_KEY")
    requester.send_gpt_request(path, 
                               line_start,
                               line_end,
                               prompt_message, 
                               open_ai_api_key, 
                               model_engine, 
                               max_tokens, 
                               number_of_outputs, 
                               temperature)

@cli.command()
@click.option('-p', '--path', type=utils.file_path, help='Path to the script')
@click.option('-ls', '--line-start', type=int, help='Starting line of the script', default=1)
@click.option('-le', '--line-end', type=int, help='Ending line of the script', default=None)
@click.option('-me', '--model-engine', type=str, help='Model Engine to be used by ChatGPT', default="text-davinci-003")
@click.option('-mt', '--max-tokens', type=int, help='Max tokens to be used by ChatGPT', default=1024)
@click.option('-n', '--number-of-outputs', type=int, help='Number of outputs by ChatGPT', default=1)
@click.option('-t', '--temperature', type=float, help='Temperature of the model by ChatGPT', default=0.5)
@click.option('-pm', '--prompt-message', type=str, help='Prompt message for ChatGPT', default='Can you explain this script to me')
def explain(path, line_start, line_end, model_engine, max_tokens, number_of_outputs, temperature, prompt_message):
    open_ai_api_key = os.environ.get("OPENAI_API_KEY")
    requester.send_gpt_request(path, 
                               line_start,
                               line_end,
                               prompt_message, 
                               open_ai_api_key, 
                               model_engine, 
                               max_tokens, 
                               number_of_outputs, 
                               temperature)

@cli.command()
@click.option('-pm', '--prompt-message', type=str, help='Prompt message for ChatGPT', default='Write a script for Hello World in Rust')
@click.option('-w', '--write-to-file', is_flag=True, help="Write to file or display on terminal")
@click.option('-p', '--path', type=str, help='Path to the script')
@click.option('-me', '--model-engine', type=str, help='Model Engine to be used by ChatGPT', default="text-davinci-003")
@click.option('-mt', '--max-tokens', type=int, help='Max tokens to be used by ChatGPT', default=1024)
@click.option('-n', '--number-of-outputs', type=int, help='Number of outputs by ChatGPT', default=1)
@click.option('-t', '--temperature', type=float, help='Temperature of the model by ChatGPT', default=0.5)
def create(prompt_message, write_to_file, path, model_engine, max_tokens, number_of_outputs, temperature):
    open_ai_api_key = os.environ.get("OPENAI_API_KEY")
    requester.send_gpt_request_create(prompt_message,
                               write_to_file, 
                               path, 
                               open_ai_api_key, 
                               model_engine, 
                               max_tokens, 
                               number_of_outputs, 
                               temperature)
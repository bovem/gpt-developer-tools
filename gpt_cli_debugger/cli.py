from argparse import ArgumentParser
import os
import sys
from model import send_gpt_request

def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise Exception("{} is not a path to file".format(string))

parser = ArgumentParser(
    prog="gcd",
    description="CLI debugging tools that uses ChatGPT to find bugs in the script",
    epilog="Remember to remove API Keys from your scripts :)",
    add_help=False
)

parser.add_argument(
    "function",  
    nargs="?",
    help="Command for debugging or explaining the script",
    choices=['debug', 'explain'],
) 

parser.add_argument('--help', action='store_true')
args, sub_args = parser.parse_known_args()

if args.help:
    if args.function is None: 
        print(parser.format_help())
        sys.exit(1)
    sub_args.append('--help')

function = "debug" if args.function is None else args.function
parser = ArgumentParser(prog="%s %s" % (os.path.basename(sys.argv[0]), function))

if function == "debug":

    parser.add_argument(
        "-p", 
        "--path",
        type=file_path,
        nargs=1,
        help="Path to the script"
    ) 

    parser.add_argument(
        "-ls", 
        "--line-start", 
        type=int,
        nargs=1,
        help="Starting line of the script",
        default=1
    ) 

    parser.add_argument(
        "-le", 
        "--line-end", 
        type=int,
        nargs=1,
        help="Ending line of the script",
        default=None
    ) 

    parser.add_argument(
        "-me", 
        "--model-engine", 
        type=str,
        nargs=1,
        help="Model Engine to be used by ChatGPT",
        default="text-davinci-003"
    ) 

    parser.add_argument(
        "-mt", 
        "--max-tokens", 
        type=int,
        nargs=1,
        help="Max Tokens to be used by ChatGPT",
        default=1024
    ) 

    parser.add_argument(
        "-n", 
        "--number-of-output", 
        type=int,
        nargs=1,
        help="Number of outputs by ChatGPT",
        default=1
    ) 

    parser.add_argument(
        "-t", 
        "--temperature", 
        type=float,
        nargs=1,
        help="Temperature for model in ChatGPT",
        default=0.5
    ) 

    parser.add_argument(
        "-pm", 
        "--prompt-message", 
        type=str,
        nargs=1,
        help="Prompt for ChatGPT",
        default="Can you debug this script for me"
    ) 
    args = parser.parse_args(sub_args)
    
    open_ai_api_key = os.environ.get("OPENAI_API_KEY")

    send_gpt_request(args.path, 
                     args.line_start,
                     args.line_end,
                     args.prompt_message, 
                     open_ai_api_key, 
                     args.model_engine, 
                     args.max_tokens, 
                     args.number_of_output, 
                     args.temperature)

elif function == "explain":

    parser.add_argument(
        "-p", 
        "--path",
        type=file_path,
        nargs=1,
        help="Path to the script"
    ) 

    parser.add_argument(
        "-ls", 
        "--line-start", 
        type=int,
        nargs=1,
        help="Starting line of the script",
        default=1
    ) 

    parser.add_argument(
        "-le", 
        "--line-end", 
        type=int,
        nargs=1,
        help="Ending line of the script",
        default=None
    ) 

    parser.add_argument(
        "-me", 
        "--model-engine", 
        type=str,
        nargs=1,
        help="Model Engine to be used by ChatGPT",
        default="text-davinci-003"
    ) 

    parser.add_argument(
        "-mt", 
        "--max-tokens", 
        type=int,
        nargs=1,
        help="Max Tokens to be used by ChatGPT",
        default=1024
    ) 

    parser.add_argument(
        "-n", 
        "--number-of-output", 
        type=int,
        nargs=1,
        help="Number of outputs by ChatGPT",
        default=1
    ) 

    parser.add_argument(
        "-t", 
        "--temperature", 
        type=float,
        nargs=1,
        help="Temperature for model in ChatGPT",
        default=0.5
    ) 

    parser.add_argument(
        "-pm", 
        "--prompt-message", 
        type=str,
        nargs=1,
        help="Prompt for ChatGPT",
        default="Can you explain this script to me"
    ) 
    args = parser.parse_args(sub_args)
    
    open_ai_api_key = os.environ.get("OPENAI_API_KEY")

    send_gpt_request(args.path, 
                     args.line_start,
                     args.line_end,
                     args.prompt_message, 
                     open_ai_api_key, 
                     args.model_engine, 
                     args.max_tokens, 
                     args.number_of_output, 
                     args.temperature)
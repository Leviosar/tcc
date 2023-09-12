import click

import steganossaurus.handlers as handlers

@click.group(
    commands = {
        "encode": handlers.encode,
        "decode": handlers.decode,
    }
)
def main():
    pass

if __name__ == "__main__":
    main()
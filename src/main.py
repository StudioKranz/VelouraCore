from config.settings import settings
from rich import print

def main():
    print("[bold green]VelouraCore Phase 2: Project Status[/bold green]")
    print(f"OPENAI_API_KEY loaded: {'Yes' if settings.OPENAI_API_KEY else 'No'}")
    print(f"HUGGINGFACE_TOKEN loaded: {'Yes' if settings.HUGGINGFACE_TOKEN else 'No'}")
    # Add more status checks as needed

if __name__ == "__main__":
    main()

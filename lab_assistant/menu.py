from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def show_menu():
    while True:
        console.clear()

        title = Panel.fit(
            "[bold cyan]Digital Lab Assistant[/bold cyan]",
            subtitle="Main Menu",
            border_style="blue"
        )
        console.print(title)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Tool", style="white")

        table.add_row("1", "Dilution calculator")
        table.add_row("2", "Media preparation calculator")
        table.add_row("3", "CFU estimator")
        table.add_row("4", "Protocol timer")
        table.add_row("5", "Exit")

        console.print(table)

        choice = Prompt.ask(
            "\n[bold yellow]Choose an option[/bold yellow]",
            choices=["1", "2", "3", "4", "5"],
            default="5"
        )

        return choice
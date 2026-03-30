import time
import datetime
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def countdown_timer(hours, minutes, seconds):
    """
    Runs a countdown timer.
    """

    try:
        total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    except ValueError:
        raise ValueError("Input must be numeric.")
    
    if float(hours) < 0 or float(minutes) < 0 or float(seconds) < 0:
        raise ValueError("Input cannot be negative.")
    
    if total_seconds == 0:
        raise ValueError("Timer must be greater than zero.")

    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        
        Text.assemble
        time_left = Text.assemble(
        ("\nTime left: ", "bold magenta"), f"{timer}")
        console.clear()
        title = Panel.fit(
            "[bold cyan]Digital Lab Assistant[/bold cyan]",
            subtitle="Protocol timer",
            border_style="blue"
        )
        console.print(title)
        console.print(time_left)

        time.sleep(1)
        total_seconds -= 1
    

def run_timer_cli():
    """
    Runs the timer in the command line interface.
    """
    console.clear()

    title = Panel.fit(
        "[bold cyan]Digital Lab Assistant[/bold cyan]",
        subtitle="Protocol timer",
        border_style="blue"
    )
    console.print(title)

    hours = Prompt.ask(
        "\n[bold yellow]Hours[/bold yellow]"
    )
    
    minutes = Prompt.ask(
        "\n[bold yellow]Minutes[/bold yellow]"
    )

    seconds = Prompt.ask(
        "\n[bold yellow]Seconds[/bold yellow]"
    )

    try:
        countdown_timer(hours, minutes, seconds)
    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        input("\nPress Enter to return to menu...")
        return
        
    alarm = Text.assemble(("\nTime's up!", "bold magenta"))
    console.print(alarm)

    input("\nPress Enter to return to menu...")
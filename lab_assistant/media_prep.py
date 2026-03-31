from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from .utils import parse_value_unit, normalize_volume, normalize_concentration, error

console = Console()

def calculate_mass_from_concentration(concentration, volume):
    """
    Calculates mass needed to achieve concentration in volume.
    Inputs may be provided with units, for example:
    - concentration: '10 g/L', '10 mg/mL'
    - volume: '0.5 L', '500 mL'

    If no units are provided, defaults are:
    - concentration: g/L
    - volume: L

    Returns mass in grams.
    """
    concentration = parse_value_unit(concentration, normalize_concentration, default_unit="g/l")
    volume = parse_value_unit(volume, normalize_volume, default_unit="l")

    mass = concentration * volume

    return mass

def run_media_prep_cli():
    """
    Runs the media prep calculator in the command line interface.
    """
    console.clear()

    title = Panel.fit(
        "[bold cyan]Digital Lab Assistant[/bold cyan]",
        subtitle="Media preparation calculator",
        border_style="blue"
    )
    console.print(title)

    concentration = Prompt.ask(
        "\n[bold yellow]Enter desired concentration (default unit: g/L)[/bold yellow]"
    )
    
    volume = Prompt.ask(
        "\n[bold yellow]Enter desired volume (default unit: L)[/bold yellow]"
    )

    try:
        mass = calculate_mass_from_concentration(concentration, volume)
    except ValueError as e:
        error(e)
        input("\nPress Enter to return to menu...")
        return
        
    answer = Text.assemble(
        ("\nMass needed: ", "bold magenta"), f"{mass:.2f} g")
    console.print(answer)

    input("\nPress Enter to return to menu...")
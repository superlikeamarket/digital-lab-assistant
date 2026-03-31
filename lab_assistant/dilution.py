from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from .utils import parse_value_unit, normalize_volume, normalize_concentration, error

console = Console()

def calculate_dilution(stock_conc, target_conc, final_volume):
    """
    Calculates stock and diluent volumes needed for a dilution.

    Inputs may be provided with units, for example:
    - concentration: '10 g/L', '10 mg/mL'
    - volume: '0.5 L', '500 mL'

    If no units are provided, defaults are:
    - concentration: g/L
    - volume: L

    Returns stock volume and diluent volume in milliliters.
    """
    
    # Normalize units
    stock_conc = parse_value_unit(stock_conc, normalize_concentration, default_unit="g/l")
    target_conc = parse_value_unit(target_conc, normalize_concentration, default_unit='g/l')
    final_volume = parse_value_unit(final_volume, normalize_volume, default_unit='l')
    
    if target_conc > stock_conc:
        raise ValueError("Target concentration cannot be greater than stock concentration.")



    
    # Calculate volumes
    stock_volume = (target_conc * final_volume) / stock_conc
    diluent_volume = final_volume - stock_volume
    return stock_volume, diluent_volume

def run_dilution_cli():
    """
    Runs the dilution calculator in the command line interface.
    """
    console.clear()

    title = Panel.fit(
        "[bold cyan]Digital Lab Assistant[/bold cyan]",
        subtitle="Dilution Calculator",
        border_style="blue"
    )
    console.print(title)

    stock_conc = Prompt.ask(
        "\n[bold yellow]Enter stock concentration (default unit: g/L)[/bold yellow]"
    )
    
    target_conc = Prompt.ask(
        "\n[bold yellow]Enter target solution concentration (default unit: g/L)[/bold yellow]"
    )
    final_volume = Prompt.ask(
        "\n[bold yellow]Enter the target solution volume (default unit: L)[/bold yellow]"
    )

    try:
        stock_volume, diluent_volume = calculate_dilution(stock_conc, target_conc, final_volume)
    except ValueError as e:
        error(e)
        input("\nPress Enter to return to menu...")
        return
        
    stock_volume_ml = stock_volume * 1000
    diluent_volume_ml = diluent_volume * 1000
    answer = Text.assemble(
        ("\nStock volume: ", "bold magenta"), f"{stock_volume_ml:.2f} mL",
        ("\nDiluent volume: ", "bold magenta"), f"{diluent_volume_ml:.2f} mL")
    console.print(answer)

    input("\nPress Enter to return to menu...")
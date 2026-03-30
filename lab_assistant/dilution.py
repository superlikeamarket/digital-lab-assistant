from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt
from rich.text import Text

console = Console()

def calculate_dilution(stock_conc, target_conc, final_volume):
    """
    Calculates volumes of stock solution and diluent needed.
    Takes as input stock concentration in mg/mL, target concentration in mg/mL 
    and final volume in mL.
    Outputs stock volume and diluent volume in mL.
    Future updates: add an option to choose units of measurement.
    """
    if stock_conc <= 0 or target_conc <= 0 or final_volume <= 0:
        raise ValueError("All values must be positive.")

    if target_conc > stock_conc:
        raise ValueError("Target concentration cannot be greater than stock concentration.")
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

    stock_conc = FloatPrompt.ask(
        "\n[bold yellow]Enter stock concentration (in mg/mL)[/bold yellow]"
    )
    
    target_conc = FloatPrompt.ask(
        "\n[bold yellow]Enter target solution concentration (in mg/mL)[/bold yellow]"
    )
    final_volume = FloatPrompt.ask(
        "\n[bold yellow]Enter the target solution volume (in mL)[/bold yellow]"
    )

    try:
        stock_volume, diluent_volume = calculate_dilution(stock_conc, target_conc, final_volume)
    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        input("\nPress Enter to return to menu...")
        return
        
    answer = Text.assemble(
        ("\nStock volume: ", "bold magenta"), f"{stock_volume:.2f} mL",
        ("\nDiluent volume: ", "bold magenta"), f"{diluent_volume:.2f} mL")
    console.print(answer)

    input("\nPress Enter to return to menu...")
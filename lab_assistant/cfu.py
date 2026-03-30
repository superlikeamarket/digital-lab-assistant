from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt, IntPrompt, Prompt
from rich.text import Text

console = Console()

def calculate_cfu(colonies, plated_volume, dilution_decimal):
    """
    Calculates the number of colony forming units in volume (mL).
    Takes as input the number of colonies, plated volume (mL) and dilution 
    decimal (as a decimal 0.0001 or an exponent -4 or 10^-4).
    Outputs CFU/mL.
    """
    if colonies <= 0:
        raise ValueError("Number of colonies must be positive.")

    if plated_volume <= 0:
        raise ValueError("Plated volume must be positive.")

    if isinstance(dilution_decimal, str) and dilution_decimal.startswith("10^"):
        dilution_decimal = int(dilution_decimal[3:])
    
    try:
        dilution_decimal = float(dilution_decimal)
    except ValueError:
        raise ValueError("The calculator accepts the following formats for the dilution decimal: 0.0001, -4, 10^-4.")

    if 0 < float(dilution_decimal) < 1:
        cfu_ml = colonies / (plated_volume * float(dilution_decimal))
    elif int(dilution_decimal) < 0:
        cfu_ml = colonies / (plated_volume * 10 ** (int(dilution_decimal)))
    else: raise
    
    if colonies < 30:
        console.print("[yellow]Warning: fewer than 30 colonies may be unreliable.[/yellow]")
    elif colonies > 300:
        console.print("[yellow]Warning: more than 300 colonies may be overcrowded.[/yellow]")



    return cfu_ml


def run_cfu_cli():
    """
    Runs the CFU estimator in the CLI.
    """
    console.clear()

    title = Panel.fit(
        "[bold cyan]Digital Lab Assistant[/bold cyan]",
        subtitle="CFU estimator",
        border_style="blue"
    )
    console.print(title)

    colonies = IntPrompt.ask(
        "\n[bold yellow]Enter the number of colonies[/bold yellow]"
    )
    
    plated_volume = FloatPrompt.ask(
        "\n[bold yellow]Enter plated volume (in mL)[/bold yellow]"
    )

    dilution_decimal = Prompt.ask(
        "\n[bold yellow]Enter dilution decimal (e.g., 0.0001, -4, 10^-4)[/bold yellow]"
    )

    try:
        cfu_ml = calculate_cfu(colonies, plated_volume, dilution_decimal)
    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        input("\nPress Enter to return to menu...")
        return
        
    answer = Text.assemble(
        ("\nCFU per mL: ", "bold magenta"), f"{cfu_ml:.2e}",)
    console.print(answer)

    input("\nPress Enter to return to menu...")
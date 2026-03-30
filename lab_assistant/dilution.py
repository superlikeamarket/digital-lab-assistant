from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt
from rich.text import Text

console = Console()

def calculate_dilution(stock_conc, target_conc, final_volume):
    """
    Calculates volumes of stock solution and diluent needed.
    Future updates: add an option to choose units of measurement.
    """
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
        "\n[bold yellow]Enter the target solution volume (in mL)[bold yellow]"
    )

    stock_volume, diluent_volume = calculate_dilution(stock_conc, target_conc, final_volume)

    answer = Text.assemble(
        ("\nStock volume:", "bold magenta"), str(stock_volume),
        ("\nDiluent volume:", "bold magenta"), str(diluent_volume))
    console.print(answer)
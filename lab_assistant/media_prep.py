from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt, Prompt
from rich.text import Text

console = Console()

def calculate_mass_from_concentration(concentration, volume):
    """
    Calculates mass needed to achieve concentration (g/L) in volume (L).
    Takes as input concentration in g and volume (with units).
    Outputs mass in g.
    """
    supported_volume_units = ['mL', 'L']

    parts = volume.split(' ')
    if len(parts) != 2:
        raise ValueError("Please enter volume like '500 mL' or '0.5 L'.")
    
    volume_value = float(parts[0])

    volume_units = parts[1]
    

    if concentration <= 0 or volume_value <= 0:
        raise ValueError("All values must be positive.")

    if volume_units not in supported_volume_units:
        raise ValueError("The calculator only supports volume in mL and L.")
    
    if volume_units == 'mL':
        mass = concentration * (volume_value / 1000)
    if volume_units == 'L':
        mass = concentration * volume_value

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

    concentration = FloatPrompt.ask(
        "\n[bold yellow]Enter desired concentration (in g/L)[/bold yellow]"
    )
    
    volume = Prompt.ask(
        "\n[bold yellow]Enter desired volume (in mL or L) and units of measurement[/bold yellow]"
    )

    try:
        mass = calculate_mass_from_concentration(concentration, volume)
    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        input("\nPress Enter to return to menu...")
        return
        
    answer = Text.assemble(
        ("\nMass: ", "bold magenta"), f"{mass:.2f} g",)
    console.print(answer)

    input("\nPress Enter to return to menu...")
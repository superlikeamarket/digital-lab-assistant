from rich.console import Console

console = Console()


def success(msg):
    console.print(f"[bold green]{msg}[/bold green]")


def error(msg):
    console.print(f"[bold red]{msg}[/bold red]")


def info(msg):
    console.print(f"[bold cyan]{msg}[/bold cyan]")


def parse_value_unit(input_str, normalize_fn, default_unit=None):
    cleaned_input = input_str.strip().lower()

    if not cleaned_input:
        raise ValueError("Input cannot be empty.")
    
    parts = cleaned_input.split(maxsplit=1)
    
    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError("Value must be a number, optionally followed by units.")

    if value <= 0:
        raise ValueError("All values must be positive.")

    if len(parts) == 2:
        unit = parts[1].strip().replace(" ", "")

    else:
        if default_unit is None:
            return value
        unit = default_unit
    
    return normalize_fn(value, unit)




def ml_to_l(value):
    return value / 1000


def ul_to_l(value):
    return value / 1_000_000


def normalize_volume(value, unit):
    unit = unit.strip().lower()

    if unit == "l":
        return value
    elif unit == "ml":
        return ml_to_l(value)
    elif unit in ["ul", "μl", "µl"]:
        return ul_to_l(value)
    else:
        raise ValueError("Unsupported unit. Use 'mL', 'L', or 'uL'.")


def mg_per_ml_to_g_per_l(value):
    return value


def mg_per_l_to_g_per_l(value):
    return value / 1000


def g_per_ml_to_g_per_l(value):
    return value * 1000


def normalize_concentration(value, unit):
    unit = unit.strip().lower()

    if unit == "mg/ml":
        return mg_per_ml_to_g_per_l(value)
    elif unit == "mg/l":
        return mg_per_l_to_g_per_l(value)
    elif unit == "g/ml":
        return g_per_ml_to_g_per_l(value)
    elif unit == "g/l":
        return value
    else:
        raise ValueError("Unsupported unit. Use 'mg/mL', 'mg/L', 'g/mL', or 'g/L'.")
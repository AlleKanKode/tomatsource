# Lave en funtkion der sætter hej efter tekst

def hejpostfix(tekst: str) -> str:
    """Postfixer en tekst med ordet hej

    Args:
        tekst (str): Strengen der skal postfixes

    Returns:
        str: En postfixet streng
    """
    return f"{tekst} hej"

if __name__ == "__main__":
    print(hejpostfix("Henrik"))
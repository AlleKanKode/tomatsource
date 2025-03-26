# Lave en funtkion der sætter hej foran tekst

def hejprefix(tekst: str) -> str:
    """Prefixer en tekst med ordet hej

    Args:
        tekst (str): Strengen der skal prefixes

    Returns:
        str: En prefixet streng
    """
    return f"hej {tekst}"

if __name__ == "__main__":
    print(hejprefix("Henrik"))

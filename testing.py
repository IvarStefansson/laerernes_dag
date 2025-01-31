"""Eksempel på enkel testing av funksjoner.

Grunnprinsippet er å teste at funksjonen gjør det den skal. Dette gjøres ved å
sammenligne forventet output med faktisk output. Det gjør vi med assert-setninger.

Eksempelet viser to funksjoner som skal legge til to til input, og en testfunksjon som
tester at funksjonen gjør det den skal.
"""

def legg_til_to(a):
    """Funksjon som legger til to til input."""
    return a + 2

def legg_til_to_med_feil(a):
    """Funksjon som legger til to til input, men med feil i funksjonen."""
    return 2

def test_at_funksjon_legger_til_to(f):
    """Tester funksjonen legg_til_to."""
    # Gjør testene (assert-setningene). Strengen i assert-setningen er en feilmelding
    # som skrives ut hvis testen feiler sånn at det er lett å se hva som gikk galt.
    assert f(2) == 4, "2 + 2 skal bli 4"
    assert f(3) == 5, "3 + 2 skal bli 5"

# Kjør testene. Hvis ingen feilmeldinger kommer, er testene bestått.
test_at_funksjon_legger_til_to(legg_til_to)  # Skal ikke gi feilmelding
test_at_funksjon_legger_til_to(legg_til_to_med_feil) # Skal gi feilmelding
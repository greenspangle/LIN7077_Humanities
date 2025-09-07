def thermostat(temperature: float) -> str:
    """If the temperature is less that 19 turn the heat on,
    if it's more than 24 turn the heat off,
    and if it's neither, leave the heat setting as it is.
    Return the string `'heat on'`, `'heat off'` or `'stet'` respectively."""
    # the three clauses in this compound if statement include all possible
    # values of temperature therefore one of them must return a value
    if temperature < 19:
        return 'heat on'
    elif temperature > 24:
        return 'heat off'
    else:
        return 'stet'

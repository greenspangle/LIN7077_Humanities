def temperature_f_to_c(temperature: float) -> float:
    """The parameter temperature represents a temperature on the
    Fahrenheit scale. Return the equivalent temperature on the Celsius scale.
    To convert a temperature from Fahrenheit to Centigrade
    first subtract thirty-two from the temperature,
    then divide that result by nine,
    then multiply by five."""
    # convert from Fahrenheit to Kelvin and then from Kelvin to Centigrade
    # as_kelvin = _f_to_k(temperature)
    # as_centigrade = _k_to_c(as_kelvin)
    # Actually no, do it as the question clues indicate
    as_centigrade = (temperature - 32) * 5 / 9
    return as_centigrade


# alternatively use Kelvin and the standard scale and
# pivot all temperature conversions through that scale

def _c_to_k(temperature: float) -> float:
    return temperature + 273.15


def _r_to_k(temperature: float) -> float:
    return temperature * 5 / 9


def _f_to_k(temperature: float) -> float:
    return (temperature - 32) * 5 / 9 + 273.15


def _k_to_c(temperature: float) -> float:
    return temperature - 273.15


def _k_to_r(temperature: float) -> float:
    return temperature * 9 / 5


def _k_to_f(temperature: float) -> float:
    return temperature * 9 / 5 - 459.67

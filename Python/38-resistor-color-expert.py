def resistor_label(colors):
    band_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    if len(colors) == 1:
        return f'{band_colors.index(colors[0])} ohms'
    elif len(colors) == 5:
        ohms = int(f'{band_colors.index(colors[0])}{band_colors.index(colors[1])}{band_colors.index(colors[2])}') * 10 ** band_colors.index(colors[3])
    else:
        ohms = int(f'{band_colors.index(colors[0])}{band_colors.index(colors[1])}') * 10 ** band_colors.index(colors[2])

    
    prefix = ""
    
    if 10 ** 3 <= ohms < 10 ** 6:
        prefix = "kilo"
        ohms /= 1000
    elif 10 ** 6 <= ohms < 10 ** 9:
        prefix = "mega"
        ohms /= 1000000

    if ohms % 1 == 0:
        ohms = int(ohms)
        
    return f'{ohms} {prefix}ohms ±{tolerance[colors[-1]]}'

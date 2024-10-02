def label(colors):
    band_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    ohms = int(f'{band_colors.index(colors[0])}{band_colors.index(colors[1])}') * 10 ** band_colors.index(colors[2])
    
    prefix = ""
    
    if 10 ** 3 <= ohms < 10 ** 6:
        prefix = "kilo"
        ohms /= 1000
    elif 10 ** 6 <= ohms < 10 ** 9:
        prefix = "mega"
        ohms /= 1000000
    elif 10 ** 9 <= ohms < 10 ** 12:
        prefix = "giga"
        ohms /= 1000000000
        
    return f'{int(ohms)} {prefix}ohms'

def value(colors):
    band_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return int(f'{band_colors.index(colors[0])}{band_colors.index(colors[1])}')

def get_rgb(color: str) -> tuple:
    match color:
        case "reds":
            return 255, 0, 0
        case "greens":
            return 0, 255, 0
        case "blues":
            return 0, 0, 255
        case "purples" | "violets":
            return 128, 0, 128
        case "teals":
            return 0, 128, 128
        case "grays":
            return 128, 128, 128
        case "yellows":
            return 255, 255, 0
        case "oranges":
            return 255, 165, 0
        case "pinks":
            return 255, 192, 203
        case "cyans":
            return 0, 255, 255
        case "browns":
            return 165, 42, 42
        case "whites":
            return 255, 255, 255
        case "blacks":
            return 0, 0, 0
        case _:
            return 0, 0, 0  # Default to black

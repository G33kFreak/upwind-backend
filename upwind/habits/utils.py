def value_per_day(value_per_week: float) -> float:
    if value_per_week != None:
        return round(value_per_week / 7, 2)
    else:
        return 0.0


def value_saved(value_per_day: float, days: int) -> float:
    return round(value_per_day * days, 2)

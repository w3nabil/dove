def fnum(value):
    try:
        return float(value) if value else 0
    except (ValueError, TypeError):
        return 0
def inum(value):
    try:
        return int(value) if value else 0
    except (ValueError, TypeError):
        return 0
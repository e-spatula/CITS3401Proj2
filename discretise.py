"""
Simple functions for discretising age, hours worked per week, capital gains and capital
losses as described in the notebook.
"""


def discretise_hours(hours):
    if hours < 10:
        return "0-9"
    elif hours < 20:
        return "10-19"
    elif hours < 30:
        return "20-29"
    elif hours < 40:
        return "30-39"
    elif hours < 50:
        return "40-49"
    elif hours < 60:
        return "50-59"
    elif hours < 70:
        return "60-69"
    elif hours < 80:
        return "70-79"
    elif hours < 90:
        return "80-89"
    else:
        return "90-99"


def discretise_age(age):
    if age < 10:
        return "0-9"
    elif age < 20:
        return "10-19"
    elif age < 30:
        return "20-29"
    elif age < 40:
        return "30-39"
    elif age < 50:
        return "40-49"
    elif age < 60:
        return "50-59"
    elif age < 70:
        return "60-69"
    elif age < 80:
        return "70-79"
    elif age < 90:
        return "80-89"
    else:
        return "90-99"


def discretise_cap_gains(gains):
    if gains < 10000:
        return "0-9K"
    elif gains < 20000:
        return "10-19K"
    elif gains < 30000:
        return "20-29K"
    elif gains < 40000:
        return "30-39K"
    elif gains < 50000:
        return "40-49K"
    elif gains < 60000:
        return "50-59K"
    elif gains < 70000:
        return "60-69K"
    elif gains < 80000:
        return "70-79K"
    elif gains < 90000:
        return "80-89K"
    else:
        return "90-99K"


def discretise_cap_loss(loss):
    if loss < 1000:
        return "0-1K"
    elif loss < 2000:
        return "1-2K"
    elif loss < 3000:
        return "2-3K"
    elif loss < 4000:
        return "3-4K"
    else:
        return "4-5K"

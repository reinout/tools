"""
Print which week of my life I'm in, according to '4000 weeks'

The nice '4000 weeks' book tries to put everything into a bit of perspective by stating
you'll live approximately 4000 weeks. 80 years * 50, to make it easy. 4000 weeks makes
your life sound distinctly finite. You cannot possibly do everything there is to do and
to visit and to read and to follow. So: you don't need to become super-efficient in
order to achieve 0.0011 instead of 0.0010 of what you could achieve. Relax a bit.

"Don't worry about tomorrow's problems, the current day has enough evil on its own".

"""

import datetime

BIRTHDAY = datetime.date(1972, 12, 25)  # A sunday, btw


def main():
    days_thankfully_alive = (datetime.date.today() - BIRTHDAY).days
    weeks_that_have_passed = days_thankfully_alive // 7
    current_week_number = int(weeks_that_have_passed) + 1
    print(f"Huidige week: nummer {current_week_number}")

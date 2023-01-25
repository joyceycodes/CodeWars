# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# my solution
import re
def validate_pin(pin):
    if len(pin) == 4 or len(pin)==6:
        for i in pin:
            pattern = '[0-9]'
            if not re.match(pattern, i):
                return False
        return True
    return False

# top solution
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

import re

password_pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}")

password = 'dsfsd@#3423'

check = password_pattern.fullmatch(password)

print(check)
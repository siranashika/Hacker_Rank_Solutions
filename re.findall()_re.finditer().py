import re
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
pattern = r"(?<=[%s])([%s]{2,})(?=[%s])" % (consonants, vowels, consonants)
matches = re.findall(pattern, input(), re.IGNORECASE)
if matches:
    print("\n".join(matches))
else:
    print("-1")

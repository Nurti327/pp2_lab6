s = "AbCdEfG Hi! 2025"
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)
from mkcombos import make_combos

key = "r"
letters = ["r", "l", "o", "d", "k", "w", "a"]

lst = make_combos(letters, 5, "a")

print(lst)

with open("/usr/share/dict/words") as f:
    words = f.read().splitlines()

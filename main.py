""" python practice by A.Talabi """

code = "India Romeo Alpha November - Alpha Bravo Alpha Delta"
words = code.split()
msg = ""

print(words)

for item in words:
    msg += item[0]

print(msg)

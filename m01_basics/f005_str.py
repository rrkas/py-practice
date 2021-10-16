s = "abcd"
s2 = "abcd"
print(s, s2)

z = s.split("b")
print(z)

sentence = "Ram is a good boy"
words = sentence.split()
print(words)

# string formattings
apples = 200
rate = 8
# method 1
out = "Ram has %s apples. Rate = Rs. %s. %s apples cost Rs. %s." % (
    apples,
    rate,
    apples,
    apples * rate,
)
print(out)

# method 2
out = "Ram has {} apples. Rate = Rs. {}. {} apples cost Rs. {}.".format(
    apples, rate, apples, apples * rate
)
print(out)

# method 3
out = f"Ram has {apples} apples. Rate = Rs. {rate}. {apples} apples cost Rs. {apples*rate}."
print(out)

print(f"{{}} {'{}'}")

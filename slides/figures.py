import matplotlib.pyplot as plt
import numpy as np

# Set fonts
plt.rc("font", size=20, family="Serif", serif="Computer Sans")
plt.rc("text", usetex=True)

# Set up a discrete probability distribution
x = np.arange(1, 4)
p = np.ones(len(x)) / len(x)

# Make the plot
plt.figure(figsize=(8, 6.5))
plt.bar(x, p, color="blue", width=0.6)
plt.ylim()
plt.gca().set_xticks([1.0, 2.0, 3.0])
plt.gca().set_yticks([0.0, 0.1, 0.2, 0.3, 0.4])
plt.ylim([0.0, 0.4])
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.title("$H = 1.0986$ nats")
plt.savefig("figures/entropy1.pdf", bbox_inches="tight")
print("Created figures/entropy1.pdf")

# Set up a discrete probability distribution
x = np.arange(5, 26)
p = np.ones(len(x)) / len(x)

# Make the plot
plt.figure(figsize=(8, 6.5))
plt.bar(x, p, color="blue", width=0.6)
plt.ylim([0.0, 0.055])
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.title("$H = 3.0445$ nats")
plt.savefig("figures/entropy2.pdf", bbox_inches="tight")
print("Created figures/entropy2.pdf")


# Set up a discrete probability distribution
x = np.hstack([np.arange(5, 21), np.arange(41, 46)])
p = np.ones(len(x)) / len(x)

# Make the plot
plt.figure(figsize=(8, 6.5))
plt.bar(x, p, color="blue", width=0.6)
plt.ylim([0.0, 0.055])
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.title("$H = 3.0445$ nats")
plt.savefig("figures/entropy3.pdf", bbox_inches="tight")
print("Created figures/entropy3.pdf")





import numpy as np
import matplotlib.pyplot as plt

# 1. Define the function (this is our "loss")
# f(x) = (x - 3)^2   -> lowest point (minimum) is at x = 3
def loss_function(x):
    return (x - 3) ** 2

# 2. Calculate the gradient (derivative)
# d/dx of (x - 3)^2  =  2 * (x - 3)
def gradient(x):
    return 2 * (x - 3)

# 3. Gradient descent
x = 10.0               # starting guess (I start far from the answer)
learning_rate = 0.1    # how big each step is
iterations = 30        # how many steps to take

x_history = [x]                    # store x at every step
loss_history = [loss_function(x)]  # store loss at every step

print("Iter |     x     |   loss   | gradient")
print("-----+-----------+----------+---------")

for i in range(iterations):
    grad = gradient(x)             # slope at current x
    x = x - learning_rate * grad   # THE UPDATE RULE: move opposite to slope

    x_history.append(x)
    loss_history.append(loss_function(x))

    print(f"{i + 1:4d} | {x:9.5f} | {loss_function(x):8.5f} | {grad:8.5f}")

print("\nFinal x:", round(x, 5), "(true minimum is 3)")

# 4 & 5. Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot I: the function curve and the path our x took
curve_x = np.linspace(-2, 12, 200)
axes[0].plot(curve_x, loss_function(curve_x), label="f(x) = (x-3)²")
path_x = np.array(x_history)
axes[0].plot(path_x, loss_function(path_x), "ro-", markersize=4, label="steps")
axes[0].set_title("Path down the curve")
axes[0].set_xlabel("x")
axes[0].set_ylabel("loss")
axes[0].legend()

# Plot II: how x changes with iterations
axes[1].plot(x_history, "g-o", markersize=3)
axes[1].axhline(3, color="gray", linestyle="--", label="true minimum (x=3)")
axes[1].set_title("Parameter x over iterations")
axes[1].set_xlabel("iteration")
axes[1].set_ylabel("x")
axes[1].legend()

# Plot III: loss over iterations
axes[2].plot(loss_history, "r-o", markersize=3)
axes[2].set_title("Loss over iterations")
axes[2].set_xlabel("iteration")
axes[2].set_ylabel("loss")

plt.tight_layout()
plt.savefig("gradient_descent_plot.png", dpi=120)
plt.show()
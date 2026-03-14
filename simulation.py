import numpy as np
import matplotlib.pyplot as plt

start_price = 100
days = 252*10
simulations = 1000

returns = np.random.normal(0.0005, 0.01, (days, simulations))
price_paths = start_price * np.exp(np.cumsum(returns, axis=0))

plt.plot(price_paths)
plt.title("Monte Carlo Stock Market Simulation")
plt.xlabel("Days")
plt.ylabel("Portfolio Value")
plt.show()

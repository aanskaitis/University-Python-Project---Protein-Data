import matplotlib.pyplot as plt

def plot_bar_show(d):
    r = range(0, len(d))
    plt.figure()

    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.tight_layout()
    plt.show()

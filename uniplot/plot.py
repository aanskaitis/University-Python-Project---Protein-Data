import matplotlib.pyplot as plt

def plot_bar_show(d):
    r = range(0, len(d))
    plt.figure()

    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.tight_layout()
    plt.show()


def plot_pie_show(d):
    labels = d.keys()
    sizes = d.values()

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()



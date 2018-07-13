def plot_bar_x(data_frame, column_name, title, x_label, y_label):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator

    ax = data_frame.plot(kind='bar', title=title, figsize=(len(data_frame[column_name]) * 3, 10), legend=True,
                         fontsize=12)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()


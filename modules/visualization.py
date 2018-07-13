def plot_bar_x(data_frame, column_name, title, x_label, y_label):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator

    ax = data_frame.plot(kind='bar', title=title, figsize=(len(data_frame[column_name]) * 3 + 3, 10), legend=True,
                         fontsize=12)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.savefig(title)


def plot_pie_x(data_frame, labels_list, y_column_name, title):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(16, 8))
    ax1 = plt.subplot(121, aspect='equal')
    data_frame.plot(kind='pie', y=y_column_name, ax=ax1, autopct='%1.1f%%', title=title,
                    startangle=90, shadow=False, labels=labels_list, legend=False, fontsize=14)
    plt.savefig(title)

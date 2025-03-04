import matplotlib.pyplot as plt

def plot_histogram(name_col, dataframe):
    plt.figure(figsize=(6, 4), facecolor='#efefef')
    plt.hist(dataframe[name_col], bins = 3, color='#38a0e8', alpha=0.7)
    plt.gca().set_facecolor('#efefef')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.title(f'{name_col} Histograma')
    plt.xticks(dataframe[name_col])
    plt.show()

def plot_bars_2col(name_col, dataframe):
    plt.figure(figsize=(6, 4), facecolor='#efefef')
    service_counts = dataframe[dataframe['Churn'] == 'Yes'][name_col].value_counts()
    service_counts = service_counts.sort_index()
    service_no_counts = dataframe[dataframe['Churn'] == 'No'][name_col].value_counts()
    service_no_counts = service_no_counts.sort_index()

    bar_width = 0.35
    index = range(len(service_counts))

    plt.bar(index, service_counts, bar_width, label='Churn', color='#e05858', alpha=0.7)
    plt.bar([i + bar_width for i in index], service_no_counts, bar_width, label='No Churn', color='#38a0e8', alpha=0.7)
    plt.gca().set_facecolor('#efefef')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.title(f'Churn por {name_col}', pad=40)
    plt.xticks([i + bar_width / 2 for i in index], service_counts.index)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13), ncol=2, frameon=False)
    
    plt.show()
       
def plot_bars_1col(name_col, dataframe):
    plt.figure(figsize=(6, 4), facecolor='#efefef')
    if dataframe[name_col].dtype == 'float64':
        dataframe[name_col] = dataframe[name_col].astype(int)
    service_counts = dataframe[dataframe['Churn'] == 'Yes'][name_col].value_counts().sort_index()
    
    bar_width = 0.35
    index = range(int(dataframe[name_col].min()), len(service_counts) + int(dataframe[name_col].min()))

    plt.bar(index, service_counts, bar_width, label='Churn', color='#e05858', alpha=0.7)
    plt.gca().set_facecolor('#efefef')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.title(f'Churn por {name_col}', pad=40)
    plt.xticks(range(0, int(dataframe[name_col].max()) + 1, 10))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.13), ncol=2, frameon=False)
    plt.show()

def plot_pie(sizes, labels, colors, titlegraphic):
    plt.figure(figsize=(8, 6), facecolor='#efefef')
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
    plt.gca().set_facecolor('#efefef')
    plt.title(f'{titlegraphic}', pad=40)
    plt.axis('equal')
    plt.show()
"""
Utility functions for generating statistics associated with k-modes clustering
"""

def print_cluster_stats(labelled_df, centroids):
    """Prints cluster deviation statistics.

    Computes the distances between all instances of a cluster in a labelled 
    df and their cluster centroid, the instance in each cluster with largest 
    deviation from their centroid, and the mean distance between all instances of
    a cluster and the centroids of the other clusters. 

    Arguments:
        labelled_df: Dataframe containing dataset with cluster labels in last column
        centroids: A list of lists containing the levels for each factor at the
        clusters centroid
    Returns:
        None
    """
    dash = 40 * "-"
    # Convert labels to ints
    labelled_df.apply(lambda x: int(x["label"]), axis=1)
    deviations = {k:[0] * len(centroids) for k in range(len(centroids))}
    count = [0] * len(centroids)
    highest_deviation = [0] * len(centroids)

    labelled_df.apply(
        lambda x: find_deviation(
            deviations, count, highest_deviation, centroids, x,
        ),
        axis=1
    )
    
    for i in range(len(centroids)):
        print(
            f"{dash}\n"
            f"Centroid {i} deviations\n"
            f"{dash}\n"
            f"Count {count[i]}\n"
            f"Largest deviation: {highest_deviation[i]}\n"
        )
        for j in range(len(centroids)):
            print(
                f"Mean deviation to cluster {j} {round(deviations[i][j]/ count[i], 2)}"
            )


def find_deviation(deviations, count, highest_deviation, centroids, row):
    """Computes deviation for an individual row in the labelled dataframe.

    The deviation for a given row from its cluster centroid is computed as well
    as its deviation from the centroids of all other clusters, and if its deviation
    from its centroid is the largest observed so far it is recorded.

    Arguments:
        deviations: dictionary mapping labels to the number of observed deviations
        with each cluster
        count: list of counts of frequency of each cluster label.
        highest_deviation: the largest deviation from the centroid observed for
        each cluster
        row: pandas series representing the row being processed in the df
    Returns:
        None
    """
    centroid = centroids[row["label"]]
    label = row["label"]

    dev_count = [0] * len(centroids) 
    for i in range(len(centroids)):
        centroid = centroids[i]
        for j in range(len(row) - 1):
            if row[j] != centroid[j]:
                dev_count[i] += 1
        
    
    for k in range(len(centroids)):
        deviations[label][k] += dev_count[k]
    
    count[label] += 1
    if dev_count[label] > highest_deviation[label]:
        highest_deviation[label] = dev_count[label]


def print_prev(factor, high_income_df, discrete_df):
    """Prints the prevalence of the levels of a particular factor in the high
    income dataset compared to the general dataset. 

    Arguments:
        factor: the factor name as a string
        high_income_df: dataframe containing only high income records
        discrete_df: dataframe containing all records
    Returns:
        None
    """
    high_income_names = high_income_df[factor].value_counts().index.to_list()
    high_income_values = high_income_df[factor].value_counts().to_list()
    high_income_values = [int(val) for val in high_income_values]

    discrete_df_names = discrete_df[factor].value_counts().index.to_list()
    discrete_df_values = discrete_df[factor].value_counts().to_list()
    discrete_df_values = [int(val) for val in discrete_df_values]

    dash = 40 * "-"
    header = "{:<26s}{:10s}{:10s}".format("Level Name", "Count", "Prevalence")
    print(f"Level prevalence report for factor {factor}")
    print(dash)
    print(header)
    print(dash)
    print("High income prevalence")
    print()
    for i in range(len(high_income_names)):
        print(
            "{:<26s}{:10d}{:10f}".format(
                high_income_names[i],
                high_income_values[i],
                round(high_income_values[i] / sum(high_income_values), 2),
            )
        )
    print()
    print(dash)
    print(header)
    print(dash)
    print("Prevalence in general dataset")
    print()
    for j in range(len(discrete_df_values)):
        print(
            "{:<26s}{:10d}{:10f}".format(
                discrete_df_names[j],
                discrete_df_values[j],
                round(discrete_df_values[j] / sum(discrete_df_values), 2),
            )
        )
    print()

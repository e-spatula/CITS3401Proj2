"""Utility functions used for printing apriori pruning rules
"""
import pandas as pd


def print_rules(df):
	"""Prints every rule in a dataframe of association mining rules
	
	Arguments:
		df: dataframe containing association mining rules
	Returns:
		None
	"""
	df.apply(lambda x: print(format_rule(x)), axis=1)
	

def format_rule(row):
	"""Formats and prints an individual association rule

	Arguments:
		row: series representing a row in a dataframe of association rules

	Returns:
		None
	"""
	antecedents = ",".join(row["antecedents"])
	consequents = ",".join(row["consequents"])
	support = row["support"]
	confidence = row["confidence"]
	lift = row["lift"]
	return (
		f"({antecedents}) -> ({consequents})\n"
		f"Support: {round(support, 2)}\n"
		f"Confidence: {round(confidence, 2)}\n"
		f"Lift: {round(lift, 2)}\n"
		f"Antecedents count: {len(row['antecedents'])}\n\n"
	)
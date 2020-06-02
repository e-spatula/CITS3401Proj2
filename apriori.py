import pandas as pd


def print_rules(df):
	df.apply(lambda x: print(format_rule(x)), axis=1)
	

def format_rule(row):
	antecedents = ",".join(row["antecedents"])
	consequents = ",".join(row["consequents"])
	support = row["support"]
	confidence = row["confidence"]
	lift = row["lift"]
	return (
		f"({antecedents}) -> ({consequents})\n"
		f"Support: {round(support, 2)}\n"
		f"Confidence: {round(confidence, 2)}\n"
		f"Lift: {round(lift, 2)}\n\n"
	)
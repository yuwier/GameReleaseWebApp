from data import game_release_table as data


def sort_filter_table(column_sort: list[str] = None, column_filter: str = None, value_filter: str = None, ascending: bool = True, page=1, limit=10):
	if column_sort is not None:
		sorted_table = data.sort_table(column=column_sort, ascending=ascending)
	else: 
		sorted_table = data.table
	if (column_filter is not None) and (value_filter is not None):
		filtered_table = data.filter_table(table=sorted_table, column=column_filter, value=value_filter)
	else:
		filtered_table = sorted_table

	start = (page - 1) * limit
	end = start + limit

	return data.table_to_dicts(filtered_table[start:end])

def get_all_unique_values():
	return data.get_all_unique_values()

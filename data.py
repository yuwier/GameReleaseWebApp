import pandas as pd

TABLE_PATH = "videogamesrelease.csv"

class GameReleaseTable():
	def __init__(self):
		# Инициализируем таблицу, меняем названия столбцов
		self.table = pd.read_csv(filepath_or_buffer=TABLE_PATH)
		self.rename_columns(columns={'Platform(s)': 'Платформа', 'Genre(s)': 'Жанр', 'Developer(s)': 'Разработчик', 'Publisher(s)': 'Издатель', 'Month': 'Месяц', 'Day': 'День', 'Title': 'Наименование'})

	def rename_columns(self, columns):
		self.table.rename(columns=columns, inplace=True)

	def get_column_unique_values(self, column: str):
		# Разделяем значения столбца через запятую
		values = self.table[column].dropna().apply(lambda string: [value.strip() for value in string.split(',')])
		unique_values = set()
		for sublist in values:
			for value in sublist:
				unique_values.add(value)
		return unique_values
	
	def get_all_unique_values(self):
		columns = ['Платформа', 'Жанр', 'Разработчик', 'Издатель', 'Месяц']
		unique_values_dict = {}
		for col in columns:
			unique_set = self.get_column_unique_values(col)
			unique_values_dict[col] = sorted(list(unique_set))
		return unique_values_dict


	def filter_table(self, column: str, value: str, table = None):
		if table is not None:
			return table[self.table[column].str.contains(value, na=False)]
		else:
			return self.table[self.table[column].str.contains(value, na=False)]

	def table_to_dicts(self, table) -> list[dict]:
		table['День'] = table['День'].astype(int)
		return table.to_dict(orient='records')
	
	def sort_table(self, column: list[str], ascending=True, table = None):
		if table is not None:
			return table.sort_values(column, ascending=ascending)
		else:
			return self.table.sort_values(column, ascending=ascending)


game_release_table = GameReleaseTable()
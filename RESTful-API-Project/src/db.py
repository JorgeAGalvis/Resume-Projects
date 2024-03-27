from typing import Any, Dict, List, Tuple, Union

import pymysql

# Type definitions
# Key-value pairs
KV = Dict[str, Any]
# A Query consists of a string (possibly with placeholders) and a list of values to be put in the placeholders
Query = Tuple[str, List]

class DB:
	def __init__(self, host: str, port: int, user: str, password: str, database: str):
		conn = pymysql.connect(
			host=host,
			port=port,
			user=user,
			password=password,
			database=database,
			cursorclass=pymysql.cursors.DictCursor,
			autocommit=True,
		)
		self.conn = conn

	def get_cursor(self):
		return self.conn.cursor()

	def execute_query(self, query: str, args: List, ret_result: bool) -> Union[List[KV], int]:
		"""Executes a query.

		:param query: A query string, possibly containing %s placeholders
		:param args: A list containing the values for the %s placeholders
		:param ret_result: If True, execute_query returns a list of dicts, each representing a returned
							row from the table. If False, the number of rows affected is returned. Note
							that the length of the list of dicts is not necessarily equal to the number
							of rows affected.
		:returns: a list of dicts or a number, depending on ret_result
		"""
		cur = self.get_cursor()
		count = cur.execute(query, args=args)
		if ret_result:
			return cur.fetchall()
		else:
			return count


	# TODO: all methods below


	@staticmethod
	def build_select_query(table: str, rows: List[str], filters: KV) -> Query:
		"""Builds a query that selects rows. See db_test for examples.

		:param table: The table to be selected from
		:param rows: The attributes to select. If empty, then selects all rows.
		:param filters: Key-value pairs that the rows from table must satisfy
		:returns: A query string and any placeholder arguments
		"""
		attributes = ", ".join(rows) if rows else '*'
		select_query = f"SELECT {attributes} FROM {table}"

		args = []
		if filters:
			where_conditions = " AND ".join([f"{key} = %s" for key in filters.keys()])
			select_query += f" WHERE {where_conditions}"
			args = list(filters.values())

		return select_query, args


	def select(self, table: str, rows: List[str], filters: KV) -> List[KV]:
		"""Runs a select statement. You should use build_select_query and execute_query.

		:param table: The table to be selected from
		:param rows: The attributes to select. If empty, then selects all rows.
		:param filters: Key-value pairs that the rows to be selected must satisfy
		:returns: The selected rows
		"""
		query, args = DB.build_select_query(table, rows, filters)
		return self.execute_query(query, args, True)

	@staticmethod
	def build_insert_query(table: str, values: KV) -> Query:
		"""Builds a query that inserts a row. See db_test for examples.

		:param table: The table to be inserted into
		:param values: Key-value pairs that represent the values to be inserted
		:returns: A query string and any placeholder arguments
		"""
		columns = ", ".join(values.keys()) if len(values.keys()) > 1 else f"{list(values.keys())[0]}"
		values_placeholder = ", ".join(["%s"] * len(values.values())) if len(values.values()) > 1 else "%s"
		values = list(values.values())
		insert_query = f"INSERT INTO {table} ({columns}) VALUES ({values_placeholder})"
		return insert_query, values

	def insert(self, table: str, values: KV) -> int:
		"""Runs an insert statement. You should use build_insert_query and execute_query.

		:param table: The table to be inserted into
		:param values: Key-value pairs that represent the values to be inserted
		:returns: The number of rows affected
		"""
		insert, values = DB.build_insert_query(table, values)
		return self.execute_query(insert, values, False)

	@staticmethod
	def build_update_query(table: str, values: KV, filters: KV) -> Query:
		"""Builds a query that updates rows. See db_test for examples.

		:param table: The table to be updated
		:param values: Key-value pairs that represent the new values
		:param filters: Key-value pairs that the rows from table must satisfy
		:returns: A query string and any placeholder arguments
		"""
		columns = ", ".join([f"{key} = %s" for key in values.keys()]) if len(values.keys()) > 1 \
			else f"{list(values.keys())[0]} = %s"
		update_query = f"UPDATE {table} SET {columns}"

		args = list(values.values())
		if filters:
			where_conditions = " AND ".join([f"{key} = %s" for key in filters.keys()]) if len(filters.keys()) > 1 \
				else f"{list(filters.keys())[0]} = %s"
			update_query += " WHERE " + where_conditions
			args += list(filters.values())

		return update_query, args

	def update(self, table: str, values: KV, filters: KV) -> int:
		"""Runs an update statement. You should use build_update_query and execute_query.

		:param table: The table to be updated
		:param values: Key-value pairs that represent the new values
		:param filters: Key-value pairs that the rows to be updated must satisfy
		:returns: The number of rows affected
		"""
		update_query, args = DB.build_update_query(table, values, filters)
		return self.execute_query(update_query, args, False)

	@staticmethod
	def build_delete_query(table: str, filters: KV) -> Query:
		"""Builds a query that deletes rows. See db_test for examples.

		:param table: The table to be deleted from
		:param filters: Key-value pairs that the rows to be deleted must satisfy
		:returns: A query string and any placeholder arguments
		"""
		delete_query = f"DELETE FROM {table}"

		args = []
		if filters:
			args = list(filters.values())
			where_conditions = " AND ".join([f"{key} = %s" for key in filters.keys()]) if len(filters.keys()) > 1 \
				else f"{list(filters.keys())[0]} = %s"
			delete_query += " WHERE " + where_conditions

		return delete_query, args

	def delete(self, table: str, filters: KV) -> int:
		"""Runs a delete statement. You should use build_delete_query and execute_query.

		:param table: The table to be deleted from
		:param filters: Key-value pairs that the rows to be deleted must satisfy
		:returns: The number of rows affected
		"""
		delete_query, args = DB.build_delete_query(table, filters)
		return self.execute_query(delete_query, args, False)

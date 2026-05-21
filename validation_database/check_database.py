###
from pathlib import Path
import duckdb

db_path = Path("src/db.sqlite3").resolve()

con = duckdb.connect()

con.execute("INSTALL sqlite")
con.execute("LOAD sqlite")

con.execute(f"""
ATTACH '{db_path}'
AS sqlite_db
(TYPE SQLITE, READ_ONLY)
""")

table_list = [data[0] for data in con.execute("SHOW TABLES FROM sqlite_db").fetchall()]

core_protein

con.execute("select * from sqlite_db.core_proteinsearch").df().to_csv("proteinsearch")

con.execute("select * from sqlite_db.core_protein").df().to_csv("protein.csv")

con.execute("select * from sqlite_db.core_proteindetail").df().to_csv("proteindetail.csv")

con.execute("select * from sqlite_db.core_proteinpdbfile").df().to_csv("proteinpdbfile.csv")
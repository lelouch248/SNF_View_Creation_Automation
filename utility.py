
# give view name and get the ddl
# def get_ddl(cursor,view_name):
#     extract_view_stm = f"SELECT GET_DDL('VIEW','{view_name}',1)"
#     cursor.execute(extract_view_stm)
#     ddl = cursor.fetchone()
#     return ddl[0] if ddl else None


def get_all_views(cursor,env):
    cursor.execute(f"show views in schema Database.Schema")
    result = cursor.fetchall()
    view_names = [f"Database.Schema.{row[1]}" for row in result]
    return view_names


# def get_bre_views(cursor,env):
#     extraction_statement = f"""select table_name from 
# Database.information_schema.tables
# where table_schema = 'Schema'
# and table_type = 'VIEW' and table_name ilike 'BRE_%';"""

#     cursor.execute(extraction_statement)
#     result = cursor.fetchall()
#     return [f"Database.Schema.{row[0]}" for row in result]



# def get_de_views(cursor,env):
#     extraction_statement = f"""
#     select table_name from 
# Database.information_schema.tables
# where table_schema = 'Schema'
# and table_type = 'VIEW' and table_name ilike 'DE_%';
# """
#     cursor.execute(extraction_statement)
#     result = cursor.fetchall()
#     return [f"Database.Schema.{row[0]}" for row in result]



# def clean_up_views(cursor,views_list):
#     for view in views_list:
#         print(f"Dropping view: {view}")
#         cursor.execute(f"DROP VIEW IF EXISTS {view}")
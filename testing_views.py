import utility
from  snowflake_con import get_snowflake_connection


conn = get_snowflake_connection()
cursor = conn.cursor()


view_list = utility.get_all_views(cursor,'PRD')


count = len(view_list)
print(f" Total views found: {count}")

for view in view_list:  
    try: 
        cursor.execute(f"explain using text SELECT top 10 * FROM {view}")
    except Exception as e:
        print(f"{view}: issue found - {e}")
    else:
        print(f"{view}: no issue found")



import snowflake.connector
import os
from dotenv import load_dotenv



load_dotenv()

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
                user=os.getenv('user'),                # Your Azure AD email
                account=os.getenv('account'),          # Your Snowflake account identifier
                warehouse=os.getenv('warehouse'),      # Your Snowflake warehouse
                database=os.getenv('database'),        # Your Snowflake database
                schema=os.getenv('schema'),            # Your Snowflake schema
                role=os.getenv('role'),                 # Role with required permissions
                authenticator='externalbrowser'
            )
        cs = conn.cursor()
        cs.execute("SELECT CURRENT_VERSION()")
        row = cs.fetchone()
        print(f"Snowflake version: {row[0]}")
        cs.close()
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

# Usage example:
# conn = get_snowflake_connection()
# print(conn)
# if conn:
#     conn.close()
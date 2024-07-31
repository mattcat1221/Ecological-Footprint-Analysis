import sqlite3
from graphviz import Digraph

# Path to the SQLite database file
db_path = '/Users/cmatthews/Desktop/Data-Analyst/Projects/Ecological-Footprint-Analysis/Global_Ecological_Footprint.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Retrieve the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create a Digraph object with settings for a more compact layout
dot = Digraph(graph_attr={'dpi': '150', 'ratio': 'compress', 'splines': 'true', 'overlap': 'false'})
dot.attr(rankdir='TB', ranksep='1', nodesep='0.5')

# Add tables and their columns to the Digraph
for table in tables:
    table_name = table[0]
    with dot.subgraph(name='cluster_' + table_name) as c:
        c.attr(label=table_name, shape='box', style='filled', color='lightgrey')
        c.node(table_name, shape='box', style='filled', color='lightgrey')
        
        # Retrieve the columns of the table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        for column in columns:
            column_name = column[1]
            c.node(f"{table_name}.{column_name}", label=column_name, shape='ellipse')
            c.edge(table_name, f"{table_name}.{column_name}")

# Add relationships based on foreign key constraints
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA foreign_key_list({table_name});")
    foreign_keys = cursor.fetchall()
    
    for fk in foreign_keys:
        from_column = fk[3]  # The column in the current table
        to_table = fk[2]     # The referenced table
        to_column = fk[4]    # The referenced column
        dot.edge(f"{table_name}.{from_column}", f"{to_table}.{to_column}", label="fk")

# Set a fixed size
dot.attr(size='10,10!')

# Close the connection
conn.close()

# Render and save the ERD diagram as an SVG file
dot.render('/Users/cmatthews/Desktop/Data-Analyst/Projects/Ecological-Footprint-Analysis/erd_diagram_with_relationships', format='svg', view=True)

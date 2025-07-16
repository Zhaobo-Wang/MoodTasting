import sqlite3

def load_sql(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    alcohol_sql  = load_sql('alcohol.sql')
    material_sql = load_sql('material.sql')

    conn = sqlite3.connect('alcohol.db')
    conn.executescript(alcohol_sql)
    conn.executescript(material_sql)
    conn.commit()
    conn.close()

    print("alcohol.db initialized")

if __name__ == "__main__":
    main()

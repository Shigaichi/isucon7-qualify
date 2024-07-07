import mysql.connector
import os

# sudo apt install python3-pip
# pip3 install mysql-connector-python==8.0.23


# データベース接続情報
db_config = {
    'user': 'isucon',
    'password': 'isucon',
    'host': 'localhost',
    'database': 'isubata',
}

# 接続を確立
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 画像データを取得するクエリ
query = "SELECT id, name, data FROM image"
cursor.execute(query)

# 保存先ディレクトリ
output_dir = '/home/isucon/isucon7-qualify/webapp/public/icons'
os.makedirs(output_dir, exist_ok=True)

# 画像をファイルに保存
for (id, name, data) in cursor:
    file_path = os.path.join(output_dir, name)
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Saved {name} to {file_path}")

# 接続を閉じる
cursor.close()
conn.close()

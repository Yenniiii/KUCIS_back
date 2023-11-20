import pymysql
import pandas as pd

class DB_API:
    def __init__(self) :
        # 데이터베이스 연결 설정
        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="1111", db="testdb", autocommit=True, charset='utf8')
        self.cur = self.conn.cursor()

    # 멤버 읽기
    def get_members(self) :
        self.cur.execute("SELECT * FROM member")
        columns = [desc[0] for desc in self.cur.description]
        data = pd.DataFrame(self.cur.fetchall(), columns=columns)
        return data

    # 멤버 생성하기
    def create_member(self, user_name) :
        self.cur.execute("INSERT INTO `member` (`name`) VALUES (%s)", (user_name,))

    # 멤버 수정하기
    def update_member(self, old_name, new_name) :
        self.cur.execute("UPDATE `member` SET `name` = %s WHERE `name` = %s", (new_name, old_name))

    # 멤버 삭제하기
    def delete_member(self, user_name) :
        self.cur.execute("DELETE FROM `member` WHERE `name` = %s", (user_name,))

    # 데이터베이서 연결 종료
    def close_connection(self):
        if self.conn:
            self.conn.close()
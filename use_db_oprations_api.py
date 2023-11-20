#######################################################################
#   use DB operations API - members table
#   
#   Created: 2023. 11. 20
#   Last Modified: 2023. 11. 20
#
#   Authors:
#      Nagyeong Choi (choi2019@pukyong.ac.kr)
#######################################################################

from db_operations_api import DB_members_API

# InternalAPI 인스턴스 생성
db_mem_api = DB_members_API()

# 데이터 조회
members_data = db_mem_api.get_members()
print("Members Data : ")
print(members_data)

# 데이터 생성
db_mem_api.create_member("이예은")

# 데이터 조회 (생성 확인)
members_data = db_mem_api.get_members()
print("Members Data : ")
print(members_data)

# 데이터 업데이트
db_mem_api.update_member("이예은", "최나경")

# 데이터 조회 (업데이트 확인)
members_data = db_mem_api.get_members()
print("Members Data : ")
print(members_data)

# 데이터 삭제
db_mem_api.delete_member("최나경")

# 데이터 조회 (삭제 확인)
members_data = db_mem_api.get_members()
print("Members Data : ")
print(members_data)

# 데이터베이스 연결 종료
db_mem_api.close_connection()

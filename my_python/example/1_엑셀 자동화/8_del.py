
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active
 # 8번째 줄에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8)


# 8번째 줄부터 3줄 삭제
# ws.delete_rows(8,3)


#2번쩨 열 부터 2줄 삭제 
# ws.delete_cols(2,2)
# ---------------------------------------------------------------------------







wb.save("sample_delet.xlsx")
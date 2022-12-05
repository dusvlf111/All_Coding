from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 8번째 줄 추가
# ws.insert_rows(8)


# 8번째 줄에 5개 줄 추가
# ws.insert_rows(8,5)


# B열 비워짐 (추가)
# ws.insert_cols(2) 

#B C D 비워짐
ws.insert_cols(2,3)





wb.save("sample_insert_cols.xlsx")
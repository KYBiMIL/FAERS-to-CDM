

# 상위 디렉터리 안에 있는 모든  .txt 파일 내용을 하나의 텍스트 파일로 합치기

import pandas as pd
import os

x = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/"   # 상위 디렉터리 경로

list = [] # 전체경로와 텍스트 파일명
list2 =[] # 전체경로를 제외한 텍스트 파일명
demo = [] # 모든 demo.txt 파일명
drug = [] # 모든 drug.txt 파일명
indi = [] # 모든 indi.txt 파일명
outc = [] # 모든 outc.txt 파일명
reac = [] # 모든 reac.txt 파일명
ther = [] # 모든 ther.txt 파일명
y2012 = [] # 2012년 모든 .txt 파일명
y2013 = [] # 2013년 모든 .txt 파일명
y2014 = [] # 2014년 모든 .txt 파일명
y2015 = [] # 2015년 모든 .txt 파일명
y2016 = [] # 2016년 모든 .txt 파일명
y2017 = [] # 2017년 모든 .txt 파일명
y2018 = [] # 2018년 모든 .txt 파일명
demo_sum=[] # 모든 년도 demo.txt 파일명
drug_sum=[] # 모든 년도 drug.txt 파일명
indi_sum=[] # 모든 년도 indi.txt 파일명
outc_sum=[] # 모든 년도 outc.txt 파일명
reac_sum=[] # 모든 년도 reac.txt 파일명
ther_sum=[] # 모든 년도 ther.txt 파일명

#
# # 전체경로와 텍스트 파일을 list에 저장
# for r, d, f in os.walk(x): # os.walk : 하위 디렉터리를 검색
#     for file in f:
#         if ".txt" in file:
#             list.append(os.path.join(r,file)) # 모든 .txt 파일을 list에 저장
#
# # 전체경로를 제외한 텍스트 파일명만 list에 저장
# for l in list:
#     file_name = os.path.basename(l)
#     list2.append(file_name)
#
# # 각 FAERS 테이블별로 저장하기
# for i in list:
#     if "demo" in i or "DEMO" in i:
#         demo.append(i)
#     elif "drug" in i or "DRUG" in i:
#         drug.append(i)
#     elif "indi" in i or "INDI" in i:
#         indi.append(i)
#     elif "outc" in i or "OUTC" in i:
#         outc.append(i)
#     elif "reac" in i or "REAC" in i:
#         reac.append(i)
#     elif "ther" in i or "THER" in i:
#         ther.append(i)

# a = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/demo_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 DEMO 파일을 리스트에 저장
# for i in demo:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "14q" in i or "14Q" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
#
# # 2018년 DEMO 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     frame.drop(columns=['auth_num', 'lit_ref', 'age_grp'], axis=0, inplace=True) # auth_num, lit_ref, age_grp 칼럼은 제거
#     # frame.rename(columns={"gndr_cod": "sex"}, inplace=True) # gndr_cod 칼럼은 sex로 이름을 변경
#     piece.append(frame)
#
# y2018_demo = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_demo.reset_index()
# y2018_demo.to_csv(a,index=False) # 인덱스 번호 제거하기


# b = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/drug_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 Drug 파일을 리스트에 저장
# for i in drug:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "14q" in i or "14Q" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
# # 2018년 Drug 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     frame.drop(columns=['prod_ai'], axis=0, inplace=True) # prod_ai 칼럼을 제거
#     piece.append(frame)
#
# y2018_drug = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_drug.reset_index()
# y2018_drug.to_csv(b,index=False) # 인덱스 번호 제거하기
#
# c = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/indi_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 Indi 파일을 리스트에 저장
# for i in indi:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "14q" in i or "14Q" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
# # 2018년 Indi 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     piece.append(frame)
#
# y2018_indi = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_indi.reset_index()
# y2018_indi.to_csv(c,index=False) # 인덱스 번호 제거하기
#
# d = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/outc_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 Outc 파일을 리스트에 저장
# for i in outc:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "14q" in i or "14Q" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
# # 2018년 Outc 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     piece.append(frame)
#
# y2018_outc = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_outc.reset_index()
# y2018_outc.to_csv(d,index=False)# 인덱스 번호 제거하기

# #
# e = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/reac_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 Reac 파일을 리스트에 저장
# for i in reac:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "2014_1" in i or "2014_2" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
# # 2018년 Reac 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     # frame['drug_rec_act'] = None # drug_rec_act 칼럼의 값은 NONE 값으로 지정
#     piece.append(frame)
#
# y2018_reac = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_reac.reset_index()
# y2018_reac.to_csv(e,index=False) # 인덱스 번호 제거하기

# # f = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/rpsr_2018.txt" # 저장할 텍스트 파일명
# #
# # # 년도별 모든 분기의 Rpsr 파일을 리스트에 저장
# # for i in rpsr:
# #     if "12q" in i or "12Q" in i:
# #         y2012.append(i)
# #     elif "13q" in i or "13Q" in i:
# #         y2013.append(i)
# #     elif "14q" in i or "14Q" in i:
# #         y2014.append(i)
# #     elif "15q" in i or "15Q" in i:
# #         y2015.append(i)
# #     elif "16q" in i or "16Q" in i:
# #         y2016.append(i)
# #     elif "17q" in i or "17Q" in i:
# #         y2017.append(i)
# #     elif "18q" in i or "18Q" in i:
# #         y2018.append(i)
# #
# # # 2018년 Rpsr 파일 piece 리스트에 저장
# # piece = []
# # for q in y2018:
# #     frame = pd.read_csv(q, sep="$", dtype=object)
# #     piece.append(frame)
# #
# # y2018_rpsr = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# # y2018_rpsr.reset_index()
# # y2018_rpsr.to_csv(f,index=False) # 인덱스 번호 제거하기
#
# g = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/ther_2018.txt" # 저장할 텍스트 파일명
#
# # 년도별 모든 분기의 Ther 파일을 리스트에 저장
# for i in ther:
#     if "12q" in i or "12Q" in i:
#         y2012.append(i)
#     elif "13q" in i or "13Q" in i:
#         y2013.append(i)
#     elif "14q" in i or "14Q" in i:
#         y2014.append(i)
#     elif "15q" in i or "15Q" in i:
#         y2015.append(i)
#     elif "16q" in i or "16Q" in i:
#         y2016.append(i)
#     elif "17q" in i or "17Q" in i:
#         y2017.append(i)
#     elif "18q" in i or "18Q" in i:
#         y2018.append(i)
#
# # 2018년 Ther 파일 piece 리스트에 저장
# piece = []
# for q in y2018:
#     frame = pd.read_csv(q, sep="$", dtype=object)
#     piece.append(frame)
#
# y2018_ther = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# y2018_ther.reset_index()
# y2018_ther.to_csv(g,index=False) # 인덱스 번호 제거하기
#
# # aa = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/demo_2018_4.txt" # 2018년 4분기 DEMO 파일명
# # bb = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/drug_2018_4.txt" # 2018년 4분기 Drug 파일명
# # cc = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/indi_2018_4.txt" # 2018년 4분기 Indi 파일명
# # dd = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/outc_2018_4.txt" # 2018년 4분기 Outc 파일명
# # ee = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/reac_2018_4.txt" # 2018년 4분기 Reac 파일명
# # ff = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/ther_2018_4.txt" # 2018년 4분기 Ther 파일명
# #
# # demo18_4 = []
# # drug18_4 = []
# # indi18_4 = []
# # outc18_4 = []
# # reac18_4 = []
# # ther18_4 = []
# # #
# # for i in list:
# #     if "demo18q4" in i or "DEMO18Q4" in i:
# #         demo18_4.append(i)
# #     elif "drug18q4" in i or "DRUG18Q4" in i:
# #         drug18_4.append(i)
# #     elif "indi18q4" in i or "INDI18Q4" in i:
# #         indi18_4.append(i)
# #     elif "outc18q4" in i or "OUTC18Q4" in i:
# #         outc18_4.append(i)
# #     elif "reac18q4" in i or "REAC18Q4" in i:
# #         reac18_4.append(i)
# #     elif "ther18q4" in i or "THER18Q4" in i:
# #         ther18_4.append(i)
# #
# # # 2018년_4분기 Ther 파일 piece 리스트에 저장
# # piece = []
# # for q in drug18_4:
# #     frame = pd.read_csv(q, sep="$", dtype=object)
# #     piece.append(frame)
# #
# # y2018_4 = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# # y2018_4.reset_index()
# # y2018_4.to_csv(bb,index=False) # 인덱스 번호 제거하기

# 모든 년도의 ther 데이터 합치기
# xx = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/ther/"   # 상위 디렉터리 경로
# h = "C:/Users/konyang/Desktop/2012.10-2018.12(FAERS)/ther.txt" # 저장할 텍스트 파일명
# # 전체경로와 텍스트 파일을 ther_sum 리스트에 저장
# for r, d, f in os.walk(xx): # os.walk : 하위 디렉터리를 검색
#     for file in f:
#         if "ther" in file:
#             ther_sum.append(os.path.join(r,file)) # 모든 .txt 파일을 ther_sum에 저장
#
#
# piece = []
# for q in ther_sum:
#     frame = pd.read_csv(q, sep=",", dtype=object)
#     # frame.drop(columns=['auth_num', 'lit_ref', 'age_grp'], axis=0, inplace=True) # auth_num, lit_ref, age_grp 칼럼은 제거
#     # frame.rename(columns={"gndr_cod": "sex"}, inplace=True) # gndr_cod 칼럼은 sex로 이름을 변경
#     piece.append(frame)
#
# yther = pd.concat(piece, axis=0) # piece 리스트의 모든 파일을 하나로 합치기
# yther.reset_index()
# yther.to_csv(h,index=False) # 인덱스 번호 제거하기


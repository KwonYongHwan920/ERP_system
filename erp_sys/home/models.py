import pymysql
# from django.db import models
# Create your models here.

############################################## 고객 관리 ###############################################
def cli_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * from clients where Isnull(clients_note)!=1"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 반품 현황 ###############################################
def now_tb():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT tb_code as '상품코드', tb_name as '상품명', tb_stock as '수량', tb_stat as '반품 상태' from take_back"
    cur.execute(sql)
    tbList = []
    for row in cur:
        tbList.append(row)
    conn.commit()
    conn.close()
    return tbList

############################################## 반품 처리 ###############################################
def Disp_tb():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE take_back, product set tb_stat='반품완료',product_stock=if(ISNULL(tb_stock)!=0,tb_stock,tb_stock+product_stock) where tb_stat='반품' and product_code=tb_code;"
    cur.execute(sql)
    conn.commit()
    conn.close()

############################################## 반품 품목 발주량 감소처리 ###############################################
def Dec_order():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE product_s, take_back,sales set sales_count=if(sales_count<tb_stock,0,sales_count-tb_stock),pro_sum=if(pro_sum<tb_stock,0,pro_sum-tb_stock), tb_stat='반품 및 발주수정완료' where tb_code=pro_code and tb_stat='반품완료' and pro_stat='입고'"
    cur.execute(sql)
    conn.commit()
    conn.close()
    
############################################## 발주 관리 ###############################################
def sales_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT product_name,brand_name as brand, product_code ,product_price=product_price*pro_sum as total_cost, if(pro_code=product_code and pro_stat='입고',pro_sum,0) as count, brand_tel, brand_account From product,sales,brand,product_s"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 브랜드 종류 갯수 업데이트 ###############################################
def UPd_brand():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE brand ,product set brand_kind_num=(select count(product_code) from product) where product_brand_name=brand_name;"
    sta = cur.execute(sql)
    conn.commit()
    conn.close()

    return sta

############################################## 상품 관리 ###############################################
def pro_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT product_name as '제품명', product_code as '제품 코드', product_price as '제품 가격', product_stock as '재고', brand_name as '브랜드명' FROM product as p right join brand as b on p.product_brand_name = b.brand_name"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 인사 관리 ###############################################
def staff_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT Sta_name as '직원명', charge_br as '담당 브랜드', sta_stat as '출근 상태', Sta_pay/30*Sta_Att as '월급계산'  FROM staff"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 입출고 관리내역 ###############################################
def proS_his():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT tb_code as '상품코드', tb_name as '상품명', tb_stock as '수량', tb_stat as '반품 상태' from take_back"
    cur.execute(sql)
    proS_hisList = []
    for row in cur:
        proS_hisList.append(row)
    conn.commit()
    conn.close()
    return proS_hisList

############################################## 입출고 업데이트 ###############################################
def proS_upd():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE product_s set pro_stat='출고',pro_sum=22"
    cur.execute(sql)
    conn.commit()
    conn.close()
    
############################################## 입고 ###############################################
def proS_In():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SET SQL_SAFE_UPDATES = 0; UPDATE product_s, sales SET sales_count=if(isNull(sales_count)!=0,pro_sum,sales_count+pro_sum) where pro_num=pro_code and pro_Stat='입고';"
    cur.execute(sql)
    conn.commit()
    conn.close()
    
############################################## 출고 ###############################################
def proS_Out():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SET SQL_SAFE_UPDATES = 0; UPDATE product_s, sales SET sales_count=if(isNull(sales_count)!=0,-1*pro_sum,sales_count+(-1*pro_sum)) where pro_num=pro_code and pro_Stat='출고';"
    cur.execute(sql)
    conn.commit()
    conn.close()
    
############################################## 재고 관리 ###############################################
def proS_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT brand_name as '브랜드명', p.product_code as '상품코드', p.product_name as '제품명', p.product_stock as '현재 수량' FROM brand, product as p right join sales as s on p.product_code = s.pro_num"
    cur.execute(sql)
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res

############################################## 재고 현황 업데이트 및 발주 ###############################################
def now_proS():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "UPDATE Product, sales, product_s set product_stock=if(isnull(product_stock)!=0,sales_count,product_stock + sales_count), sales_count=0, pro_Stat=if(pro_stat='입고','입고종료',if(pro_stat='출고','출고종료',NULL)) Where product_code=pro_num and (pro_Stat='출고' or pro_stat='입고') ;"
    cur.execute(sql)
    proSList = []
    for row in cur:
        proSList.append(row)
    conn.commit()
    conn.close()
    return proSList

############################################## 재무 관리 ###############################################
def fin_manage():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT brand_name as '브랜드' , sum(product_price*pro_sum) as '총판매가격',sum(product_price*pro_sum)/10*1.5 as '실 수익', sum(product_price*pro_sum)/10 as '수수료',sum(product_price*pro_sum)/10*3 as '브랜드 수익', brand_kind_num as '브랜드 품목 종류 갯수', if(brand_name=charge_br,sta_name,NULL) as '담당자' from product, product_s, brand, staff order by '총판매가격' desc"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 직원 출근 업데이트 ###############################################
def sta_upd():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT brand_name as '브랜드' , sum(product_price*pro_sum) as '총판매가격',sum(product_price*pro_sum)/10*1.5 as '실 수익', sum(product_price*pro_sum)/10 as '수수료',sum(product_price*pro_sum)/10*3 as '브랜드 수익', brand_kind_num as '브랜드 품목 종류 갯수', if(brand_name=charge_br,sta_name,NULL) as '담당자' from product, product_s, brand, staff order by '총판매가격' desc"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

############################################## 상품 추가 ###############################################
def insert_prod(query):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "INSERT into PRODUCT (product_code,product_name,product_brand_name,product_price,product_stock) VALUES (%s,%s,%s,%s,%s);"
    cur.execute(sql, query)
    conn.commit()
    conn.close()

############################################## 상품 현황 ###############################################
def pro_view():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='dydghks5210', db='erp_sys', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM PRODUCT;"
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res
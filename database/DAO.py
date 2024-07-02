from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(s.`datetime`) as anno, count(distinct s.id) as tot
from sighting s 
where s.country ='us' 
group by year(s.`datetime`)"""

        cursor.execute(query)

        for row in cursor:
            result.append(f"{row["anno"]} ({row["tot"]})")

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.state as stato
from sighting s 
where s.country ='us' and year(s.`datetime`) =%s
group by s.state 
having count(s.id)>0"""

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(row["stato"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(id1,anno,id2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
from (select s.`datetime` as d1
from sighting s 
where s.country ='us' and s.state =%s
and year(s.`datetime`)=%s) as t1,
(select s.`datetime` as d2
from sighting s 
where s.country ='us' and s.state =%s
and year(s.`datetime`)=%s) as t2
where d1<d2
"""

        cursor.execute(query,(id1,anno,id2,anno,))

        for row in cursor:
            result=row["peso"]
        cursor.close()
        conn.close()
        return result

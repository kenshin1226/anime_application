from flask import Flask,render_template,session, request,redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route('/list')
def list():
        conn=sqlite3.connect('anime.db')
        cur=conn.cursor()
        cur.execute('select * from anime')
        anime_list=cur.fetchall()
        print("@12",anime_list)
        return render_template('list.html',a_list=anime_list)
@app.route('/input')
def input():
      return render_template('input.html')
@app.route('/input2',methods=["POST"])
def input2():
      title=request.form.get("title")
      season=request.form.get("season")
      star=request.form.get("star")
      comment=request.form.get("comment")
      postuser=request.form.get("postuser")
      print("title=",title)
      conn=sqlite3.connect('anime.db')
      cur=conn.cursor()
      cur.execute("INSERT INTO anime(animename,season,star,comment,postuser) VALUES(?,?,?,?,?)"
      ,(title,season,star,comment,postuser))
      conn.commit()
      conn.close()
      return  redirect(url_for("list"))
# if __name__ =="__main__":
app.run(debug=True)
from flask import Flask, render_template,request,redirect
import sqlite3
app = Flask(__name__) 

@app.route('/') 
def root():
    try:
        con = sqlite3.connect("Inventory.db")
        sql = ''' 
    SELECT * FROM Product
    '''
        cur = con.execute(sql)
        data = cur.fetchall()
        return render_template("products_2.html", my_list = data) #with edit link
    except sqlite3.DatabaseError as ex:
        print(ex)
    con.close()


@app.route('/form') ## return a web form
def form():
    return render_template("form_1.html")
 
@app.route('/insert', methods=["POST", "GET"]) ## using post
def insert_data():
    if request.method == "GET":
        return "GET request not supported"
    else:
        try:
            con = sqlite3.connect("Inventory.db")

            image_name = None
            upload_file = request.files.get("image")
            if upload_file:
                image_name = upload_file.filename
                upload_file.save(f"static/images/{image_name}")
            else:
                print("No image file uploaded")

            sql = 'INSERT INTO Product VALUES(?,?,?,?)'
            cur = con.execute(sql,
                            (request.form["product"], 
                            request.form["description"],
                            request.form["price"], image_name ))
            print(f"{cur.rowcount} row inserted" )
            con.commit()
            
        except sqlite3.DatabaseError as ex:
            print(ex)
    con.close()
    return redirect("/")

@app.route("/edit/<product_name>")
def edit(product_name):
    try:
        con = sqlite3.connect("Inventory.db")
        sql = 'SELECT * FROM Product WHERE ProductName = ?'

        cur = con.execute(sql, [product_name])
        product = cur.fetchone()
            
    except sqlite3.DatabaseError as ex:
            print(ex)    
    con.close()
    return render_template("form_2.html", product=product)
    
@app.route('/update/<product_name>', methods=["POST", "GET"]) ## using post
def update_data(product_name):
    if request.method == "GET":
        return "GET request not supported"
    else:
        try:
            con = sqlite3.connect("Inventory.db")

            image_name = None
            upload_file = request.files.get("image")
            if upload_file:
                image_name = upload_file.filename
                upload_file.save(f"static/images/{image_name}")
            else:
                print("No image file uploaded")

            sql = '''UPDATE Product SET 
            ProductName = ?,
            Description = ?,
            Price = ?,
            Image = ?
            WHERE ProductName = ?'''
            cur = con.execute(sql,
                            (request.form["product"], 
                            request.form["description"],
                            request.form["price"], image_name,  product_name))
            print(f"{cur.rowcount} row udated" )
            con.commit()
                
        except sqlite3.DatabaseError as ex:
            print(ex)

    return redirect("/")

app.run() 
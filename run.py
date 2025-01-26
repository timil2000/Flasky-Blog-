# from flaskBlog import app
#
# if __name__ == '__main__':
#     with app.app_context():
#         # db.create_all()
#         # print("Database and tables created in MySQL successfully.")
#         #
#         # user_1= User (username='Corey' ,email='C@demo.com' , password='password')
#         # user_2= User (username='Corey1' ,email='C@demo1.com' , password='password1')
#         # user_3= User (username='Corey2' ,email='C@demo2.com' , password='password2')
#         # user_4= User (username='Corey3' ,email='C@demo3.com' , password='password3')
#         #
#         # db.session.add(user_1)
#         # db.session.add(user_2)
#         # db.session.add(user_3)
#         # db.session.add(user_4)
#         # db.session.commit()
#         print("Data added in MySQL successfully.")
#     app.run(debug=True)

from Flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)
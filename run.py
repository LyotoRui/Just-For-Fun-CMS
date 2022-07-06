from app import create_app, init_db, init_mail, init_migrate

app = create_app()

db = init_db(app=app)

mail = init_mail(app=app)

migrate = init_migrate(app=app, db=db)

if __name__ == '__main__':
    app.run()
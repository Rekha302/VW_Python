class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/task_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "task-management-secret-key"



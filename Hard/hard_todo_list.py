"""
TO-DO LIST

About  
To-Do list can improve your work and personal life. 
You can use it to reduce the stress in your life and get more done in less time. 
It also helps you become more reliable for other people and save time for the best things in life. 
So let's implement it!

Learning outcomes  
To-Do list that will help you manage your tasks. 
You will practice using loops, conditions and statement branches. 
And also you will learn the basics of SQLAlchemy to manage SQLite database on python!

Stage 1
Create a simple program that prints today's tasks. 

Stage 2
Build your first potion. Set up the database. 

Stage 3
Tasks should have deadlines. Implement the ability to set deadlines. 

Stage 4
There are also completed tasks. Let's delete them.

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def add_task():

    task_description = str(input("\nEnter task:\n"))
    deadline_input = str(input("Enter deadline: yyyy-mm-dd\n"))
    task_deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
    print("The task has been added!\n")
    new_row = Table(task=task_description, deadline=task_deadline)
    session.add(new_row)
    session.commit()


def print_today():
    today = datetime.today()
    rows = session.query(Table).filter(Table.deadline == today.date()).all()
    print("\nToday " + str(today.strftime("%d %b")) + ":")
    if len(rows) == 0:
        print("Nothing to do!\n")
    else:
        for x in range(0, len(rows)):
            row = rows[x]
            print(str(x+1) + ". " + str(row.task))


def print_week():
    today = datetime.today()
    for x in range(0, 7):
        rows = session.query(Table).filter(Table.deadline < (today + timedelta(days=x))).filter(Table.deadline > (today + timedelta(days=x-1))).order_by(Table.deadline).all()
        print("\n" + (today + timedelta(days=x)).strftime("%A %d %b"))
        for z in range(0, len(rows)):
            row = rows[z]
            if row is None:
                print("Nothing to do!\n")
            else:
                print(str(z+1) + ". " + str(row.task))


def print_all():
    rows = session.query(Table).order_by(Table.deadline).all()
    print("\nAll tasks:")
    if len(rows) == 0:
        print("Nothing to do!\n")
    else:
        for x in range(0, len(rows)):
            row = rows[x]
            print(str(x+1) + ". " + str(row.task) + ". " + str(row.deadline.strftime("%d %b")))


def missed_task():
    today = datetime.today()
    rows = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline).all()
    print("\nMissed tasks:")
    for x in range(0, len(rows)):
        row = rows[x]
        print(str(x+1) + ". " + str(row.task) + ". " + str(row.deadline.strftime("%d %b")))


def delete_task():
    print("Choose the number of the task you want to delete:\n")
    rows = session.query(Table).order_by(Table.deadline).all()
    for x in range(0, len(rows)):
        row = rows[x]
        print(str(x+1) + ". " + str(row.task) + ". " + str(row.deadline.strftime("%d %b")))
    task_to_delete = int(input()) - 1
    print("The task has been deleted!\n")
    specific_row = rows[task_to_delete]
    session.delete(specific_row)
    session.commit()


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


while True:

    user = int(input("""\n1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit\n"""))

    if user == 0:
        print("Bye!")
        exit()
    elif user == 1:
        print_today()
    elif user == 2:
        print_week()
    elif user == 3:
        print_all()
    elif user == 4:
        missed_task()
    elif user == 5:
        add_task()
    elif user == 6:
        delete_task()

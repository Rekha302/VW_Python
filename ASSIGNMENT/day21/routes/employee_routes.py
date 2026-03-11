
from flask import Blueprint, render_template, session
from models import Employee
from decorators import role_required
from extensions import db

employee_bp = Blueprint("employee", __name__)


# View all employees
@employee_bp.route("/employees")
@role_required(["admin", "manager"])
def employees():

    if session["role"] == "manager":
        employees = Employee.query.filter_by(manager_id=session["user_id"]).all()
    else:
        employees = Employee.query.all()

    return render_template("employees.html", employees=employees)


# View employee profile
@employee_bp.route("/employee/<int:id>")
@role_required(["admin", "manager", "employee"])
def profile(id):

    employee = Employee.query.get(id)

    return render_template("profile.html", employee=employee)


# Edit employee
@employee_bp.route("/employee/<int:id>/edit")
@role_required(["admin", "manager", "employee"])
def edit_employee(id):

    if session["role"] == "employee" and session["user_id"] != id:
        return "Employees can edit only their own profile"

    return f"Editing employee {id}"


# Delete employee (Admin only)
@employee_bp.route("/employee/<int:id>/delete")
@role_required(["admin"])
def delete_employee(id):

    employee = Employee.query.get(id)

    db.session.delete(employee)
    db.session.commit()

    return "Employee deleted successfully"
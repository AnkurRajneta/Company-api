import enum

class TableName:
    USER = "user"
    ROLE = "role"
    EMPLOYEES = "employees"
    PERMISSIONS = "permissions"
    ROLEPERMISSIONASSOCIATION = "rolepermissionassociation"
    USERROLEASSOCIATION = "userroleassociation"

class UserRoleEnum(str,enum.Enum):
    ADMIN = "Admin"
    HR = "Hr"
    EMPLOYEES = "Employees"

class ActiveEnum(str,enum.Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class Permissions(str, enum.Enum):
    CREATE_EMPLOYEE_CONTROLLER = "create_employee_controller"
    UPDATE_EMPLOYEES_BY_ID = "update_employees_by_id"
    DELETE_USER_BY_ID_CONTROLLER = "delete_user_by_id_controller"
    CREATE_ROLE_CONTROLLER = "create_role_controller"
    UPDATE_ROLE_BY_ID_CONTROLLER = "update_role_by_id_controller"
    DELETE_ROLE_BY_ID_CONTROLLER = "delete_role_by_id_controller"
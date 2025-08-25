import enum

class TableName:
    USER = "user"
    ROLE = "role"
    EMPLOYEES = "employees"

class UserRoleEnum(str,enum.Enum):
    ADMIN = "Admin"
    HR = "Hr"
    EMPLOYEES = "Employees"

class ActiveEnum(str,enum.Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
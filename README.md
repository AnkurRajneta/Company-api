

<img width="942" height="857" alt="image" src="https://github.com/user-attachments/assets/9f38817c-85c1-4a3a-8c38-f48338074582" />


This project is an Office API built using FastAPI and integrated with Swagger UI for API documentation.

It includes three primary models:

1. User – Represents individuals accessing the system.

2. Role – Defines the level of access (e.g., Admin, HR).

3. Employee – Stores employee-related information.

The system is implemented with Role-Based Access Control (RBAC) to manage permissions:

a) Admin can create, update, and delete both employees and roles.

b) HR can create, update, and delete employees but cannot manage roles.

c) Employees are not permitted to perform any operations


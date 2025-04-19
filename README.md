# Student-Record-Manager

This is a Flask-based Student Management System API that allows you to add, update, delete, and retrieve student records. The backend is connected to a database for storing student information.

## Features
- **Add Student**: Add a new student record.
- **Update Student**: Update an existing student’s marks and grade.
- **Retrieve All Students**: Fetch all student records.
- **Retrieve a Specific Student**: Get details of a specific student by roll number.
- **Delete Student**: Remove a student record from the database.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/gayatrirkaware/Student-Record-Manager.git


   ```
2. Navigate to the project directory:
   ```sh
   cd Student-Record-Manager-api
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/` | Serves the dashboard page |
| `GET` | `/students` | Retrieves all students from the database |
| `GET` | `/student/<student_id>` | Retrieves details of a student by roll number |
| `POST` | `/add-student` | Adds a new student record |
| `POST` | `/update-student/<student_id>` | Updates a student's marks and grade |
| `GET` | `/delete-student/<student_id>` | Deletes a student record |

## Request & Response Examples

### Add Student
#### Request:
```json
POST /add-student
{
  "name": "John Doe",
  "rollNo": "101",
  "courses": ["Math", "Science"],
  "marks": 85,
  "grade": "A"
}
```
#### Response:
```json
{
  "message": "Student data added successfully"
}
```

### Update Student
#### Request:
```json
POST /update-student/101
{
  "marks": 90,
  "grade": "A+"
}
```
#### Response:
```json
{
  "message": "Student data updated successfully"
}
```

## Technologies Used
- Python (Flask)
- MongoDB (Database)
- HTML Templates (Dashboard)

## Notes
- Ensure MongoDB is running before starting the API.
- Modify `project_config.py` to adjust database connection settings.


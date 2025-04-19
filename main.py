from flask import Flask,jsonify,render_template,request, send_from_directory
from app.database import get_db
import project_config

students_collection = get_db()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard.html')
   

@app.route('/<page>')
def serve_page(page):
    return send_from_directory('templates', page)

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get("name","")
    rollNo = data.get("rollNo","")
    courses = data.get("courses","")
    marks = data.get("marks","")
    grade = data.get("grade","")
    response = students_collection.find_one({"name":name,"rollNo":rollNo})
    if not response:
        students_collection.insert_one({"name":name,"rollNo":rollNo,"courses":courses,"marks":marks,"grade":grade})
        return jsonify({"message": "Student data added successfully"})
    else:
        return jsonify({"message": "Student data Already Exists"})


@app.route('/update-student/<student_id>', methods=['POST'])
def update_student(student_id):
    data = request.json
    up_marks = data.get("marks")
    up_grade = data.get("grade")
    response = students_collection.find_one({"rollNo":student_id})
    if response:
        students_collection.update_one({"rollNo":student_id},{"$set":{"marks":up_marks,"grade":up_grade}})
        return jsonify({"message": "Student data updated successfully"})
    else:
        return jsonify({"message": "Student Id wont Exists"})
    


@app.route('/students', methods=['GET'])
def get_students():
    response = list(students_collection.find({}, {"_id": 1, "name": 1, "rollNo": 1, "courses": 1, "marks": 1, "grade": 1}))
    for student in response:
        student["_id"] = str(student["_id"])  
    return jsonify(response)


@app.route('/student/<student_id>', methods=['GET'])
def get_student(student_id):
    response = students_collection.find_one({"rollNo": student_id}, {"_id": 1, "name": 1, "rollNo": 1, "courses": 1, "marks": 1, "grade": 1})
    if response:
        response["_id"] = str(response["_id"])  
        return jsonify(response)
    return jsonify({"message": "Student not found"}), 404


@app.route('/delete-student/<student_id>', methods=['GET'])
def delete_student(student_id):
    response = students_collection.find_one({"rollNo": student_id})
    if not response:
        return jsonify({"message": "Student Id does not exists"})
    else:
        students_collection.delete_one({"rollNo": student_id})
        return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= 8085, debug=True)

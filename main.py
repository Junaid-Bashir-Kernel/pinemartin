from flask import Flask , render_template , Response
from AttendanceProject import camera_output
import csv

app=Flask(__name__)


@app.route("/")
def home():
 return render_template("home.html")

@app.route('/video_feed')
def video_feed():
    return Response(camera_output(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/attendance")
def attendance():
       data=[]
       with open("Attendance.csv") as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            
                return render_template('attendance.html', data=data)    


if __name__ == "__main__":
    app.run(debug=True)
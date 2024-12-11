from flask import Flask , request,render_template

from certificates.certificate import cerf

app=Flask(__name__)

@app.route("/")
def index():
  return render_template('certificate_form.html')

@app.route("/generate",methods=['POST'])
def generate():
  name = request.form.get('name')
  course = request.form.get('course')
  all_classes = request.form.get('all_classes')
  all_assignments = request.form.get('all_assignment')
  print(name)
  print(course)
  print(all_assignments)
  print(all_classes)
  certificate= cerf(name,course,all_classes,all_assignments)
  person=certificate.generate_certificate()
  name=person['name']
  print(name)
  course=person['course']
  print(course)

  if all_classes=='YES' and all_assignments=='YES':
    return render_template('generate.html',name=name,course=course)
  
  else:
    return render_template('not_complited.html')




if __name__=='__main__':
  app.run(debug=True)





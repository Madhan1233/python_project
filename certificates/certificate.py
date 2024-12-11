


class cerf:
  def __init__(self,name, course,classes,assignment):
    self.name=name
    self.course=course
    self.classes=classes
    self.assignment=assignment
    
  def generate_certificate(self):
    dicts={'name':self.name,
             'course':self.course}
    return dicts
      
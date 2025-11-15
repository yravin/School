from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50, null=True, blank=True)
    student_majar = models.CharField(max_length=100, default="", blank=True) 
    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


class Teacher(models.Model):
    SUBJECTS = [
        ('គណិតវិទ្យា', 'គណិតវិទ្យា'),
        ('ភាសាខ្មែរ' , 'ភាសាខ្មែរ'),
        ('រូបវិទ្យា', 'រូបវិទ្យា'),
        ('គីមីវិទ្យា', 'គីមីវិទ្យា'),
        ('python', 'Python'),
    ]

    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, choices=SUBJECTS)
    classes = models.CharField(max_length=200, default="មិនកំណត់")

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Class(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="classes")

    def __str__(self):
        return f"Class {self.name} (Teacher: {self.teacher.name})"


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, null=True, blank=True, default=None)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, default=None)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, default=None)

    day = models.CharField(max_length=10, choices=[
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ], default='Mon')

    start_time = models.TimeField(null=True, blank=True, default=None)
    end_time = models.TimeField(null=True, blank=True, default=None)
    student_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.classroom} - {self.subject} ({self.day})"
    
class Classgood(models.Model) :
    Class_id =models.CharField(max_length=200, unique=True)  
    Teacher_name = models.CharField(max_length=200, null=True) 
    name_class = models.CharField(max_length=200)
    student_cunte = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_class
    

class ScoreStudent(models.Model):
    CLASSES = [
        ('ថ្នាក់ទី12A','ថ្នាក់ទី12A'),
        ('ថ្នាក់ទី12B','ថ្នាក់ទី12B'),
        ('ថ្នាក់ទី12C','ថ្នាក់ទី12C'),
        ('ថ្នាក់ទី12D','ថ្នាក់ទី12D'),
        ('ថ្នាក់ទី11A','ថ្នាក់ទី11A'),
        ('ថ្នាក់ទី11B','ថ្នាក់ទី11B'),
        ('ថ្នាក់ទី11C','ថ្នាក់ទី11C'),
        ('ថ្នាក់ទី11D','ថ្នាក់ទី11D'),
        ('ថ្នាក់ទី10A','ថ្នាក់ទី10A'),
        ('ថ្នាក់ទី10B','ថ្នាក់ទី10B'),
        ('ថ្នាក់ទី10C','ថ្នាក់ទី10C'),
        ('ថ្នាក់ទី10D','ថ្នាក់ទី10D'),
    ] 
    classes = models.CharField(max_length=200 ,choices=CLASSES , default='ថ្នាក់ទី12A') 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Khmer = models.IntegerField(default=0)
    Math = models.IntegerField(default=0)
    Physics = models.IntegerField(default=0)
    chmisty = models.IntegerField(default=0)
    English = models.IntegerField(default=0)
    Morality = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    AI = models.IntegerField(default=0)
    Computer = models.IntegerField(default=0)

    # ✅ គណនាពិន្ទុសរុប
    @property
    def total_score(self):
        return (
            self.Math + self.Khmer + self.Physics +
            self.chmisty + self.English + self.Morality +
            self.python + self.AI + self.Computer
        )

    # ✅ គណនាមធ្យមភាគ
    @property
    def average_score(self):
        subjects = 9  # ចំនួនមុខវិជ្ជា
        return self.total_score / subjects

    # ✅ គណនានិន្ទេស
    @property
    def grade(self):
        avg = self.average_score
        if avg >= 90:
            return "A+"
        elif avg >= 85:
            return "A"
        elif avg >= 80:
            return "B+"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"{self.student.name}"   # assuming Student model has "name"

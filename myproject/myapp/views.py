from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Teacher, Schedule, Student, ClassRoom, Classgood, ScoreStudent
from .form import TeacherForm, ScheduleForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json

def home(request):
    teachers = Teacher.objects.count()
    classes = ClassRoom.objects.count()
    students = Student.objects.count()
    schedules = Schedule.objects.count()
    
    return render(request, 'index.html', {
        'teachers': teachers,
        'classes': classes,
        'students': students,
        'schedules': schedules,
    })


def student(request): 
    students = Student.objects.all()
    return render(request, 'myapp/student.html', {'students': students})


def schedule(request):
    DAY_MAP = {
        'Monday': ('Mon', 'ច័ន្ទ'),
        'Tuesday': ('Tue', 'អង្គារ'),
        'Wednesday': ('Wed', 'ពុធ'),
        'Thursday': ('Thu', 'ព្រហស្បតិ៍'),
        'Friday': ('Fri', 'សុក្រ'),
        'Saturday': ('Sat', 'សៅរ៍'),
        'Sunday': ('Sun', 'អាទិត្យ')
    }
    
    today_eng = timezone.now().strftime('%A')
    today_code, today_kh = DAY_MAP.get(today_eng, ('Mon', today_eng))
    
    schedules = Schedule.objects.filter(day=today_code)
    
    
    context = {
        'today': today_kh,
        'schedules': schedules,
    }
    return render(request, 'myapp/schedule.html', context)


def teacher_list(request):
    # Initialize the form
    teacher_form = TeacherForm(prefix="teacher")

    if request.method == "POST":
        action = request.POST.get('action')
        teacher_id = request.POST.get('teacher_id')

        # Add new teacher
        if action == "save_teacher":
            teacher_form = TeacherForm(request.POST, prefix="teacher")
            if teacher_form.is_valid():
                teacher_form.save()
                return redirect('teacher_list')

        # Delete teacher
        elif action == "delete_teacher" and teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.delete()
                return redirect('teacher_list')
            except Teacher.DoesNotExist:
                pass

    # List all teachers
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers,
        'teacher_form': teacher_form,
    }
    return render(request, 'myapp/techer.html', context)


def classgood(request):
    Topclass= Classgood.objects.all()
    students = Student.objects.filter(name ='Teacher_name')

    return render(request, 'myapp/classgood.html',{"Topclass":Topclass, "students": students})


def base(request):
    return render(request, 'base.html')

def adminmanagermentSythem(request):
    teacher_form = TeacherForm(prefix="teacher")
    schedule_form = ScheduleForm(prefix="schedule")

    if request.method == "POST":
        action = request.POST.get('action')

        if action == "save_teacher":  # Save teacher
            teacher_form = TeacherForm(request.POST, prefix="teacher")
            if teacher_form.is_valid():
                teacher_form.save()
                return redirect("teacher_list")

        elif action == "save_schedule":  # Save schedule
            schedule_form = ScheduleForm(request.POST, prefix="schedule")
            if schedule_form.is_valid():
                schedule_form.save()
                return redirect("schedule")

    context = {
        "teacher_form": teacher_form,
        "schedule_form": schedule_form,
    }
    
    return render(request, 'myapp/adminSythem.html', context)

def User(request) :
    return render (request ,"myapp/user.html")

#API______________________________________________________________________________

@csrf_exempt
def admin_login_api(request):
    if request.method == 'POST':
        try:
           data = json.loads(request.body)
           username = data.get('username')
           password = data.get('password')

           user = authenticate(username=username, password=password)
           if user is not None and user.is_staff:
                login(request, user)
                return JsonResponse({'message': 'ចូលប្រើប្រាស់ជោគជ័យ!'})
           else:
                return JsonResponse({'message': 'ឈ្មោះអ្នកប្រើ ឬពាក្យសម្ងាត់មិនត្រឹមត្រូវ'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'JSON មិនត្រឹមត្រូវ'}, status=400)
    return JsonResponse({'message': 'មិនគាំទ្រទេ'}, status=405)   

#API______________________________________________________________________________
#API______________________________________________________________________________
def score(request):
    student_score =  ScoreStudent.objects.all()
    students = Student.objects.values_list('name', flat=True)

    return render(request, 'myapp/score.html', {
        'student_score': student_score,
        'students' : 'students'
        
    })





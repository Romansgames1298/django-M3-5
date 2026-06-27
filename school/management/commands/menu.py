from django.core.management.base import BaseCommand
from school.models import Subject, Teacher, SchoolClass, Student, Schedule, Grade
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        while True:
            print("\n===== SCHOOL MENU =====")
            print("1. Добавить предмет")
            print("2. Добавить учителя")
            print("3. Добавить класс")
            print("4. Добавить ученика")
            print("5. Добавить расписание")
            print("6. Добавить оценку")
            print("0. Выход")

            choice = input("Выберите пункт: ")

            # ---------------- SUBJECT ----------------
            if choice == "1":
                name = input("Название предмета: ")
                desc = input("Описание: ")

                if Subject.objects.filter(name=name).exists():
                    print("Такой предмет уже есть!")
                else:
                    Subject.objects.create(name=name, description=desc)
                    print("Предмет добавлен")

            # ---------------- TEACHER ----------------
            elif choice == "2":
                first = input("Имя: ")
                last = input("Фамилия: ")
                subject_id = input("ID предмета: ")

                try:
                    subject = Subject.objects.get(id=subject_id)
                    Teacher.objects.create(
                        first_name=first,
                        last_name=last,
                        subject=subject
                    )
                    print("Учитель добавлен")
                except:
                    print("Предмет не найден")

            # ---------------- CLASS ----------------
            elif choice == "3":
                name = input("Название класса: ")
                year = input("Год обучения: ")

                if SchoolClass.objects.filter(name=name).exists():
                    print("Такой класс уже есть!")
                else:
                    SchoolClass.objects.create(
                        name=name,
                        study_year=year
                    )
                    print("Класс добавлен")

            # ---------------- STUDENT ----------------
            elif choice == "4":
                first = input("Имя: ")
                last = input("Фамилия: ")
                class_id = input("ID класса: ")

                try:
                    school_class = SchoolClass.objects.get(id=class_id)
                    Student.objects.create(
                        first_name=first,
                        last_name=last,
                        school_class=school_class
                    )
                    print("Ученик добавлен")
                except:
                    print("Класс не найден")

            # ---------------- SCHEDULE ----------------
            elif choice == "5":
                day = input("День (Mon/Tue/Wed/Thu/Fri): ")
                time = input("Время (HH:MM): ")
                subject_id = input("ID предмета: ")
                class_id = input("ID класса: ")
                teacher_id = input("ID учителя: ")

                try:
                    subject = Subject.objects.get(id=subject_id)
                    school_class = SchoolClass.objects.get(id=class_id)
                    teacher = Teacher.objects.get(id=teacher_id)

                    Schedule.objects.create(
                        day_of_week=day,
                        start_time=datetime.strptime(time, "%H:%M").time(),
                        subject=subject,
                        school_class=school_class,
                        teacher=teacher
                    )
                    print("Расписание добавлено")
                except:
                    print("Ошибка: проверь ID")

            # ---------------- GRADE ----------------
            elif choice == "6":
                student_id = input("ID ученика: ")
                subject_id = input("ID предмета: ")
                grade_value = input("Оценка: ")
                date = input("Дата (YYYY-MM-DD): ")

                try:
                    student = Student.objects.get(id=student_id)
                    subject = Subject.objects.get(id=subject_id)

                    Grade.objects.create(
                        student=student,
                        subject=subject,
                        grade=grade_value,
                        date=date
                    )
                    print("Оценка добавлена")
                except:
                    print("Ошибка: проверь данные")

            # ---------------- EXIT ----------------
            elif choice == "0":
                break

            else:
                print("Неверный выбор")
import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation


def fix_marks(name):
    schoolkid_marks = Mark.objects.filter(schoolkid__full_name__contains=name,
                                          points__lt=4)
    for mark in schoolkid_marks:
        mark.points = random.randint(4, 5)
        mark.save()


def remove_chastisements(name):
    chastisement = Chastisement.objects.filter(schoolkid__full_name__contains=name)
    for mark in chastisement:
        mark.delete()


def create_commendation(name, subject, lesson_date):
    praise = ['Молодец!',
              'Отлично!',
              'Хорошо!',
              'Гораздо лучше, чем я ожидал!',
              'Ты меня приятно удивил!',
              'Великолепно!',
              'Прекрасно!',
              'Это как раз то, что нужно!',
              'Я тобой горжусь!',
              'С каждым разом у тебя получается всё лучше!',
              'Мы с тобой не зря поработали!' 'Я вижу, как ты стараешься!'
              ]
    try:
        child = Schoolkid.objects.get(full_name__icontains=name)
        lesson = Lesson.objects.filter(subject__title__icontains=subject,
                                       year_of_study=child.year_of_study,
                                       group_letter=child.group_letter)[0]
        Commendation.objects.create(text=random.choices(praise)[0],
                                    created=lesson_date,
                                    schoolkid_id=child.id,
                                    subject_id=lesson.subject_id,
                                    teacher_id=lesson.teacher_id)
    except ObjectDoesNotExist:
        print("Школьника с таким именем не существует. Проверьте имя и запустите функцию снова")
    except MultipleObjectsReturned:
        print("Найдено более одного ученика с таким именем. Проверьте имя и запустите функцию снова")

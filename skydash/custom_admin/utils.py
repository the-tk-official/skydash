from django.db.models import Q

from users.models import Profile
from courses.models import Course


def filterForAccount(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        course = Course.objects.filter(title__icontains=search_query)

        accounts = Profile.objects.distinct().filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(gender__icontains=search_query) |
            Q(prof__icontains=search_query) |
            Q(course__in=course)
        )

    else:
        accounts = Profile.objects.all()

    return accounts, search_query


def filterForCourses(request):
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        courses = Course.objects.distinct().filter(
            Q(title__icontains=search_query)
        )
    else:
        search_query = ''
        courses = Course.objects.all()

    return courses, search_query

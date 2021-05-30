from django.urls import include, re_path
from v1.apps.v1_comments import urls as com_urls
from v1.apps.v1_course_actions import urls as ca_urls
from v1.apps.v1_courses import urls as c_urls
from v1.apps.v1_lesson_actions import urls as la_urls
from v1.apps.v1_lessons import urls as l_urls
from v1.apps.v1_materials import urls as m_urls
from v1.apps.v1_tasks import urls as t_urls
from v1.apps.v1_themes import urls as th_urls
from v1.apps.v1_users import urls as u_urls

urlpatterns = [
    # re_path(r"^comments/", include(com_urls)),
    # re_path(r"^course_actions/", include(ca_urls)),
    # re_path(r"^courses/", include(c_urls)),
    # re_path(r"^lesson_actions/", include(la_urls)),
    # re_path(r"^lessons/", include(l_urls)),
    # re_path(r"^materials/", include(m_urls)),
    # re_path(r"^tasks/", include(t_urls)),
    # re_path(r"^themes/", include(th_urls)),
    # re_path(r"^users/", include(u_urls)),
]

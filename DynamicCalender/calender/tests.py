from django.test import TestCase
from .models import Events, Calender
from django.contrib.admin.sites import AdminSite
from .admin import CalenderModelAdmin

# Create your tests here.
class CalendarTestCase(TestCase):

    def model_returned(self):
        self.model = Calender.objects.create(user="Albert", title="test Calender", description="test decsc", start_date='2022-08-07', end_date='2022-08-08', start_time='07:49:15', end_time='08:10:25', created_at='2022-08-06 14:56:56', updated_at='2022-08-07 15:25:35')


class ModelAdminTest(TestCase):
    pass
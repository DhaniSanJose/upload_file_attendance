# attendance/models.py
from django.db import models

class AttendanceRecord(models.Model):
    employee_id = models.CharField(max_length= 100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time_in = models.DateTimeField(null=True, blank=True)
    break_in = models.DateTimeField(null=True, blank=True)
    break_out = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
            return self.employee_id
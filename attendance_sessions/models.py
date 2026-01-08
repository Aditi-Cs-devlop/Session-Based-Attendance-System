from django.db import models
from django.conf import settings
import uuid


class Session(models.Model):
    session_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_sessions'
    )

    def __str__(self):
        return f"Session {self.session_id} | Active: {self.is_active}"


class AttendanceRecord(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    participant_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('recognized', 'Recognized'),
            ('unrecognized', 'Unrecognized')
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.participant_name} - {self.status}"

from django.db import models
from django.conf import settings
from django.utils import timezone


class Attendance(models.Model):
    session = models.OneToOneField(
        'Session',
        on_delete=models.CASCADE,
        related_name='attendance'
    )

    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    total_faces = models.PositiveIntegerField()
    recognized_count = models.PositiveIntegerField()
    unrecognized_count = models.PositiveIntegerField()

    submitted_at = models.DateTimeField(default=timezone.now)

    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance for Session {self.session.session_id}"

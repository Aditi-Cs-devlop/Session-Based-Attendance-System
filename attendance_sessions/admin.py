from django.contrib import admin
from .models import Session, AttendanceRecord


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'is_active', 'start_time', 'end_time', 'created_by')
    list_filter = ('is_active', 'start_time')
    search_fields = ('session_id',)


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'status', 'session', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('participant_name',)

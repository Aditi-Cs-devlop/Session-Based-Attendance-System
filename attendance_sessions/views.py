from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Session


@login_required
def start_session(request):
    # Check if an active session already exists
    active_session = Session.objects.filter(is_active=True).first()
    if active_session:
        return JsonResponse({
            "error": "A session is already active",
            "session_id": str(active_session.session_id)
        }, status=400)

    # Create a new session
    session = Session.objects.create(
        created_by=request.user,
        is_active=True
    )

    return JsonResponse({
        "message": "Session started successfully",
        "session_id": str(session.session_id),
        "start_time": session.start_time
    }, status=201)


from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Session


@login_required
@require_POST
def stop_session(request):
    try:
        session = Session.objects.get(is_active=True)
    except Session.DoesNotExist:
        return JsonResponse(
            {"error": "No active session to stop"},
            status=400
        )

    session.is_active = False
    session.end_time = timezone.now()
    session.save()

    return JsonResponse({
        "message": "Session stopped successfully",
        "session_id": session.session_id,
        "end_time": session.end_time
    })
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def session_control_page(request):
    return render(request, "attendance_sessions/session_control.html")


from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Session, Attendance


@login_required
@require_POST
def final_submit_attendance(request):
    # 1. Check active session
    session = Session.objects.filter(is_active=True).first()
    if not session:
        return JsonResponse(
            {"error": "No active session"},
            status=400
        )

    # 2. Prevent duplicate attendance
    if hasattr(session, 'attendance'):
        return JsonResponse(
            {"error": "Attendance already submitted for this session"},
            status=400
        )

    # 3. Get counts from request
    try:
        total_faces = int(request.POST.get("total_faces"))
        recognized = int(request.POST.get("recognized_count"))
        unrecognized = int(request.POST.get("unrecognized_count"))
    except (TypeError, ValueError):
        return JsonResponse(
            {"error": "Invalid attendance data"},
            status=400
        )

    # 4. Save attendance
    attendance = Attendance.objects.create(
        session=session,
        submitted_by=request.user,
        total_faces=total_faces,
        recognized_count=recognized,
        unrecognized_count=unrecognized
    )

    return JsonResponse({
        "message": "Attendance submitted successfully",
        "attendance_id": attendance.id,
        "session_id": str(session.session_id)
    }, status=201)

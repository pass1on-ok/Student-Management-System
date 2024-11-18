# views.py
from rest_framework import viewsets

from attendance.models import Attendance
from attendance.permissions import IsNotStudent
from attendance.serializers import AttendanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsNotStudent]

    def get_serializer_context(self):
        """
        Передаём запрос в контекст сериализатора, чтобы он мог проверять роль пользователя.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
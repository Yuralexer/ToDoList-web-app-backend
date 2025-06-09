from rest_framework import serializers

from .models import Task


class TaskDetailSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display', 
        read_only=True
    )
    class Meta:
        model = Task
        fields = (
            "id", 
            "title", 
            "description", 
            "created_at",
            "deadline",
            "status",
            "status_display",
        )
        read_only_fields = ("created_at",)

class TaskListSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(
        source='get_status_display', 
        read_only=True
    )
    class Meta:
        model = Task
        fields = (
            "id", 
            "title", 
            "deadline",
            "status",
            "status_display",
        )
        read_only_fields = ("created_at",)

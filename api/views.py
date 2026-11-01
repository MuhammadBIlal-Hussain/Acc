from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Membership


class HealthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"status": "ok", "service": "ledgerforge-api", "phase": 1})


class MeView(APIView):
    def get(self, request):
        memberships = Membership.objects.filter(
            user=request.user,
            is_active=True,
            company__is_active=True,
        ).select_related("company")
        return Response(
            {
                "id": str(request.user.id),
                "username": request.user.username,
                "email": request.user.email,
                "companies": [
                    {
                        "id": str(membership.company.id),
                        "name": membership.company.name,
                        "currency": membership.company.base_currency,
                        "role": membership.role,
                    }
                    for membership in memberships
                ],
            }
        )

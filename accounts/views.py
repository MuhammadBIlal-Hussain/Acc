from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Membership


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        memberships = (
            Membership.objects.filter(user=self.request.user, is_active=True, company__is_active=True)
            .select_related("company")
        )
        context["memberships"] = memberships
        context["active_company"] = memberships.first()
        return context


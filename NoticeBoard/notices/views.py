from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from .forms import NoticeForm
from .models import Notice, Reaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .signals import send_accepted_reaction
from .filters import ReactionFilter

class NoticeCreate(LoginRequiredMixin, CreateView):
    form_class = NoticeForm
    model = Notice
    template_name = 'notice_create.html'
    success_url = '/board/'

    def form_valid(self, form):
        notice = form.save(commit=False)
        notice.author = self.request.user
        return super().form_valid(form)

class NoticeList(ListView):
    model = Notice
    ordering = '-datetime_created'
    template_name = 'notices.html'
    context_object_name = 'notices'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NoticeDetail(LoginRequiredMixin, DetailView):
    model = Notice
    template_name = 'notice_detail.html'
    context_object_name = 'notice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        notice = context['notice']
        context['reactions'] = Reaction.objects.filter(notice=notice, is_accepted=True).order_by('-datetime_created')
        context['current_user'] = user
        return context

    def post(self, request, *args, **kwargs):
        text = request.POST['reaction_text']
        user = request.user
        notice = Notice.objects.filter(pk=self.kwargs['pk']).first()
        Reaction.objects.create(text=text, user=user, notice=notice)

        return redirect(request.path)

class Dashboard(LoginRequiredMixin, ListView):
    model = Reaction
    ordering = '-datetime_created'
    template_name = 'dashboard.html'
    context_object_name = 'reactions'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(notice__author=user)
        self.filterset = ReactionFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def post(self, request, *args, **kwargs):
        if 'reaction_accept' in request.POST.keys():
            pk = int(request.POST['reaction'])
            reaction = Reaction.objects.filter(pk=pk).first()
            reaction.is_accepted = True
            reaction.save()
            send_accepted_reaction(pk)
        if 'reaction_delete' in request.POST.keys():
            pk = int(request.POST['reaction'])
            reaction = Reaction.objects.filter(pk=pk).first()
            reaction.delete()
        return redirect(request.path)

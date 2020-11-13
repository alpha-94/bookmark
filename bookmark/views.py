from django.shortcuts import render

# Create your views here.
# CRUD : create / read / update / delete

# List - read

# 클래스형 뷰, 함수형 뷰
# 웹페이지에 접속한다 -> 페이지를 본다.
# URL 을 입력 -> 웹 서버가 뷰를 찾아서 동작 시킨다. -> 응답

# 제네릭 뷰 관련
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Bookmark
from django.urls import reverse_lazy


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']

    # urls 내부에 있는 path 를 들어가게끔 하는 변수
    success_url = reverse_lazy('list')

    # 웹 상 templateDoesNotExist 나올 때 bookmark/bookmark_form.html 으로 나오는데 이걸 _create 로 바꿔주는 변수
    # edit 내부에 있는 클래스 경우는 form 으로 되어있는경우가 있어서 template_name_suffix를 이용하여 변경한다 .
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
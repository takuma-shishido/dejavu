from django.shortcuts import render

# Create your views here.
def create_novel(request):
    create_novel_info = ["title", "imag"]
    context = {"create_novel_info" : create_novel_info}
    return render(request, "create_novel.html", context)
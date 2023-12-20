from django.shortcuts import render



# Create your views here.
def write_continue(request):
    sample_book_info = ["title", "img", "description", "story"]

    context = {"sample_book_info" : sample_book_info}
    return render(request, "write_continue.html", context)
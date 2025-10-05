from django.shortcuts import render

# Fake "database"
announcements = [
    {'id': 1, 'title': 'Welcome to the Site', 'content': 'This is the first announcement. We are glad to have you here! mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'},
    {'id': 2, 'title': 'Exam Schedule', 'content': 'The midterm exam will start next week. Please review your notes and prepare accordingly. mdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'},
    {'id': 3, 'title': 'Holiday Notice', 'content': 'There will be no classes on Friday due to a public holiday.'},
]

def home(request):
    return render(request, 'announcements/home.html')

def list_announcements(request):
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a['id'] == id), None)
    return render(request, 'announcements/detail.html', {'announcement': announcement})

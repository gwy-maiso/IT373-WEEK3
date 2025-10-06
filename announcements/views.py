from django.shortcuts import render

# Fake "database"
announcements = [
    {'id': 1, 'title': 'Welcome to the Site', 'content': 'This is the first announcement. We are glad to have you here!'},
    {'id': 2, 'title': 'Exam Schedule', 'content': 'The midterm exam will start next week. Please review your notes and prepare accordingly.'},
    {'id': 3, 'title': 'IMPORTANT ADVISORY', 'content': 'As per the evaluation and assessment of the medical team, and to ensure everyone’s health and safety following reported cases of Hand, Foot, and Mouth Disease (HFMD), the EVSU-Main Campus will shift to online/asynchronous classes from October 6 to 10, 2025. Students are strictly advised not to enter the campus, while TechnoMart will be temporarily closed during this period. Non-teaching personnel are also directed to conduct thorough sanitation in their respective work areas. Let’s all do our part to maintain a safe and healthy campus. Please monitor your health and report any flu-like symptoms immediately. Stay safe, EVSUnistas!'},
]

def home(request):
    return render(request, 'announcements/home.html')

def list_announcements(request):
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a['id'] == id), None)
    return render(request, 'announcements/detail.html', {'announcement': announcement})

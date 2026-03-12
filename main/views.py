from django.shortcuts import render
from .models import Correct, Incorrect


def index_view(request):
    correct = None
    incorrects = None
    message = None

    word = request.GET.get('word', "").strip()
    if word:
        if 'x' not in word.lower() and 'h' not in word.lower():
            message = "So'z tarkibida Xx yoki Hh mavjud emas!"
        else:

            correct = Correct.objects.filter(word__icontains=word).first()
            if correct:
                incorrects = correct.incorrect_set.all()

            else:
                incorrect = Incorrect.objects.filter(word__icontains=word).first()
                if incorrect:
                    correct = incorrect.correct
                    incorrects = correct.incorrect_set.all()
                else:
                    message = "Ba'zada bunday so'z mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
    }
    return render(request, "index.html", context)

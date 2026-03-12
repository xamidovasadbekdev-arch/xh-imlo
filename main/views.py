# from django.shortcuts import render
# from .models import Correct, Incorrect
#
#
# def index_view(request):
#     correct = None
#     incorrects = None
#     message = None
#
#     word = request.GET.get('word', "").strip()
#     if word:
#         if 'x' not in word.lower() and 'h' not in word.lower():
#             message = "So'z tarkibida Xx yoki Hh mavjud emas!"
#         else:
#
#             correct = Correct.objects.filter(word=word).first()
#             if correct:
#                 incorrects = correct.incorrect_set.all()
#
#             else:
#                 incorrect = Incorrect.objects.filter(word=word).first()
#                 if incorrect:
#                     correct = incorrect.correct
#                     incorrects = correct.incorrect_set.all()
#                 else:
#                     message = "Ba'zada bunday so'z mavjud emas!"
#
#     context = {
#         'correct': correct,
#         'incorrects': incorrects,
#         'message': message,
#     }
#     return render(request, "index.html", context)

from django.shortcuts import render
from .models import Correct, Incorrect
from .ai_utils import get_word_variants


def index_view(request):
    correct = None
    incorrects = None
    message = None
    ai_used = False

    word = request.GET.get('word', "").strip()

    if word:
        if 'x' not in word.lower() and 'h' not in word.lower():
            message = "So'z tarkibida Xx yoki Hh mavjud emas!"
        else:
            # Avval DBdan qidir
            correct = Correct.objects.filter(word__iexact=word).first()

            if correct:
                incorrects = correct.incorrect_set.all()
            else:
                incorrect = Incorrect.objects.filter(word__iexact=word).first()
                if incorrect:
                    correct = incorrect.correct
                    incorrects = correct.incorrect_set.all()
                else:
                    # DBda yo'q — AI dan so'ra
                    ai_result = get_word_variants(word)

                    if ai_result and ai_result.get('correct'):
                        correct, _ = Correct.objects.get_or_create(
                            word=ai_result['correct']
                        )
                        for inc_word in ai_result.get('incorrects', []):
                            Incorrect.objects.get_or_create(
                                word=inc_word,
                                correct=correct
                            )
                        incorrects = correct.incorrect_set.all()
                        ai_used = True
                    else:
                        message = "Bu so'z topilmadi!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
        'ai_used': ai_used,
    }
    return render(request, "index.html", context)


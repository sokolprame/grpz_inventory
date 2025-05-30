from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from orders.models import Order
from components.models import Component

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте данные.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/registration/register.html', {'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(created_by=request.user).prefetch_related('orderitem_set')
    components = Component.objects.filter(orderitem__order__created_by=request.user).distinct()
    print(f"Загружено заказов для {request.user.username}: {orders.count()}")
    print(f"Компоненты пользователя {request.user.username}: {components.count()}")
    return render(request, 'users/profile.html', {'orders': orders, 'components': components})

@login_required
def download_profile_report(request):
    user = request.user
    components = Component.objects.filter(orderitem__order__created_by=user).distinct()

    # Генерация LaTeX-кода
    latex_content = r"""
    \documentclass[a4paper,12pt]{article}
    \usepackage[utf8]{inputenc}
    \usepackage[russian]{babel}
    \usepackage{geometry}
    \geometry{margin=1in}
    \usepackage{array}
    \usepackage{booktabs}

    \begin{document}

    \begin{center}
        \Huge{\textbf{Отчёт по профилю пользователя}}
        \vspace{0.5cm}
        \Large{\textbf{GRPZ Inventory}}
    \end{center}

    \section*{Информация о пользователе}
    \begin{tabular}{ll}
        \toprule
        \textbf{Поле} & \textbf{Значение} \\
        \midrule
        Имя пользователя & """ + user.username + r""" \\
        Email & """ + (user.email if user.email else "Не указан") + r""" \\
        Дата регистрации & """ + user.date_joined.strftime("%d.%m.%Y %H:%M") + r""" \\
        \bottomrule
    \end{tabular}

    \section*{Детали (Компоненты)}
    """
    
    if not components:
        latex_content += r"\textit{У пользователя пока нет компонентов.}" + "\n"
    else:
        latex_content += r"""
        \begin{center}
            \begin{tabular}{|m{5cm}|m{3cm}|m{5cm}|}
                \hline
                \textbf{Название} & \textbf{Количество} & \textbf{Изображение} \\
                \hline
        """
        for component in components:
            image_info = component.image.url if component.image else "Изображение отсутствует"
            latex_content += r"            " + component.name.replace("&", r"\&") + r" & " + str(component.quantity) + r" & " + image_info.replace("&", r"\&").replace("_", r"\_") + r" \\ \hline" + "\n"
        latex_content += r"""
            \end{tabular}
        \end{center}
        """

    latex_content += r"""
    \end{document}
    """

    # Возвращаем LaTeX-код как PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="profile_report_{user.username}.pdf"'
    response.write(latex_content.encode('utf8'))
    return response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from configuration.models import (Anagrafica,
                                  Lesson,
                                  Pricelist,
                                  Trainer,
                                  User
                                  )
from configuration.forms import (AnagraficaForm,
                                 LessonForm,
                                 PricelistForm,
                                 TrainerForm
                                 )


@login_required
def anagrafica_detail(request):
    gym_data = get_object_or_404(Anagrafica, pk=1)
    form = AnagraficaForm(request.POST or None)
    context = {
        'gym_data': gym_data,
        'form': form
    }
    return render(request, 'configurazione/anagrafica.html', context)


@login_required
def anagrafica_edit(request, post_id):
    gym_data = get_object_or_404(Anagrafica, pk=post_id)
    if gym_data.author != request.user:
        return redirect('configuration:anagrafica_detail', gym_data.pk)
    form = AnagraficaForm(
        request.POST or None,
        instance=gym_data
    )
    if form.is_valid():
        form.save()
        return redirect('configuration:anagrafica_detail', gym_data.pk)
    context = {
        'gym_data': gym_data,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'configurazione/anagrafica.html', context)


@login_required
def lessons(request):
    lesson_list = Lesson.objects.all().order_by('-pub_date')
    context = {
        'lesson_list': lesson_list
    }
    return render(request, 'configurazione/lessons.html', context)


@login_required
def lesson_detail(request, post_id):
    one_lesson = get_object_or_404(Lesson, pk=post_id)
    context = {
        'one_lesson': one_lesson
    }
    return render(request, 'configurazione/lesson_detail.html', context)


@login_required
def lesson_create(request):
    form = LessonForm(request.POST or None)
    if not form.is_valid():
        return render(request,
                      'configurazione/lesson_create.html',
                      {'form': form})
    lesson = form.save(commit=False)
    lesson.author = request.user
    lesson.save()
    return redirect('configuration:lessons')


@login_required
def lesson_edit(request, post_id):
    template = 'configurazione/lesson_create.html'
    one_lesson = get_object_or_404(Lesson, pk=post_id)
    if one_lesson.author != request.user:
        return redirect(
            'configuration:lesson_detail', post_id
        )
    form = LessonForm(
        request.POST or None,
        instance=one_lesson
        )
    breakpoint()
    print(form)
    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.author = request.user
        lesson.save()
        return redirect(
            'configuration:lesson_detail', post_id
        )
    return render(request, template, {
        'form': form, 'is_edit': True, 'one_lesson': one_lesson
    })


@login_required
def lesson_delete(request, post_id):
    one_lesson = get_object_or_404(Lesson, pk=post_id)
    if one_lesson.author == request.user:
        one_lesson.delete()
    return redirect('configuration:lessons')


@login_required
def trainers(request):
    trainer_list = Trainer.objects.all().order_by('-pub_date')
    context = {
        'trainer_list': trainer_list
    }
    return render(request, 'configurazione/trainers.html', context)


@login_required
def trainer_create(request):
    form = TrainerForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.author = request.user
        data.save()
        return redirect('configuration:trainers', data.author)
    else:
        form.errors
    return render(request,
                  'configurazione/trainer_create.html',
                  {'form': form})


@login_required
def trainer_detail(request, post_id):
    one_trainer = get_object_or_404(Trainer, pk=post_id)
    context = {
        'one_trainer': one_trainer
    }
    return render(request, 'configurazione/trainer_detail.html', context)


@login_required
def trainer_edit(request, post_id):
    one_trainer = get_object_or_404(Trainer, pk=post_id)
    if one_trainer.author != request.user:
        return redirect('configuration:trainer_detail', one_trainer.pk)
    form = TrainerForm(
        request.POST or None,
        instance=one_trainer
    )
    if form.is_valid():
        form.save()
        return redirect('configuration:lesson_detail', one_trainer.pk)
    context = {
        'one_trainer': one_trainer,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'configurazione/trainer_create.html', context)


@login_required
def pricelists(request):
    pricelist_list = Pricelist.objects.all().order_by('-pub_date')
    context = {
        'pricelist_list': pricelist_list
    }
    return render(request, 'configurazione/pricelists.html', context)


@login_required
def pricelist_create(request):
    form = PricelistForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.author = request.user
        data.save()
        return redirect('configuration:pricelists', data.author)
    else:
        form.errors
    return render(request,
                  'configurazione/pricelist_create.html',
                  {'form': form})


@login_required
def pricelist_detail(request, post_id):
    one_pricelist = get_object_or_404(Pricelist, pk=post_id)
    context = {
        'one_pricelist': one_pricelist
    }
    return render(request, 'configurazione/pricelist_detail.html', context)


@login_required
def pricelist_edit(request, post_id):
    one_pricelist = get_object_or_404(Pricelist, pk=post_id)
    if one_pricelist.author != request.user:
        return redirect('configuration:pricelist_detail', one_pricelist.pk)
    form = PricelistForm(
        request.POST or None,
        instance=one_pricelist
    )
    if form.is_valid():
        form.save()
        return redirect('configuration:lesson_detail', one_pricelist.pk)
    context = {
        'one_pricelist': one_pricelist,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'configurazione/pricelist_create.html', context)

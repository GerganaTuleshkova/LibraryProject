from django.shortcuts import render, redirect

from LibraryProject.library_app.forms import CreateProfileForm, AddBookForm, EditProfileForm, DeleteProfileForm, \
    DeleteProfileFormDisabled
from LibraryProject.library_app.helpers_functions import get_profile
from LibraryProject.library_app.models import Book
from LibraryProject.settings import BASE_DIR


def home(request):
    profile = get_profile()
    if profile is None:
        return profile_create(request)
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'home-with-profile.html', context)


def book_add(request):
    if request.method == 'POST':
        # create form with POST
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create empty form
        form = AddBookForm()

    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')


def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # create form with POST
        form = AddBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create empty form
        form = AddBookForm(instance=book)

    context = {
        'form': form,
        'book': book
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def profile_create(request):
    if request.method == 'POST':
        # create form with POST
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create empty form
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        # create form with POST
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        # create empty form
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'POST':
        # create form with POST
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create form with profile details
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)

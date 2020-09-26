from django.shortcuts import render
from django.contrib import messages
from sudoku.sudoku_solver import Solver
from sudoku.sudoku_validate import Validation
import requests

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        sudoku = list(request.POST.items())[1:-1]
        values = [i[1] for i in sudoku]
        sudoku_matrix = [values[i:i+9] for i in range(0, 81, 9)]
        context["sudoku"] = sudoku_matrix
        s1 = Validation()
        if s1.isValidSudoku(sudoku_matrix):
            s = Solver()
            s.solveSudoku(sudoku_matrix)
        else:
            messages.error(request, 'The input is not valid.')



    context['range'] = range(9)
    return render(request, 'sudoku/home.html', context)
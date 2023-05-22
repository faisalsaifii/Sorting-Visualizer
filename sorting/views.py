from django.shortcuts import render, redirect
from sorting.models import SortingAlgorithm


def visualize_sorting(request):
    if request.method == 'POST':
        algorithm_name = request.POST['algorithm_name']
        numbers = request.POST['numbers']
        sorted_numbers = perform_sorting(algorithm_name, numbers)
        sorting_algorithm = SortingAlgorithm(
            name=algorithm_name, numbers=numbers)
        return render(request, 'visualizer.html', {'numbers': sorted_numbers, 'sorting_algorithm': sorting_algorithm})
    return render(request, 'base.html')


def perform_sorting(algorithm_name, numbers):
    num_list = list(map(int, numbers.split(',')))
    if algorithm_name == 'bubble_sort':
        sorted_list = bubble_sort(num_list)
    elif algorithm_name == 'selection_sort':
        sorted_list = selection_sort(num_list)
    elif algorithm_name == 'insertion_sort':
        sorted_list = insertion_sort(num_list)
    else:
        sorted_list = bubble_sort(num_list)

    sorted_numbers = ','.join(map(str, sorted_list))
    return sorted_numbers


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

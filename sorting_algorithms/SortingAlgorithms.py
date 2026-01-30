from random import randint
import json

"""SortingAlgorithm master class that will be inherited by other sorting classes"""
class SortingAlgorithm:
    def __init__(self, num_elements: int=10, min_value: int=0, max_value: int=500) -> None:
        self._number_of_elements: int = num_elements # attribute that represents number of elements to sort
        self._min_element_value: int = min_value # attribute that represents minimum bounded value of element
        self._max_element_value: int = max_value # attribute that represents maximum bounded value of element
        self._data: list = [] # attribute that represents the list containing elements (dataset)
    
    # method to generate random data values
    def generate_data(self) -> None:
        self._data: list = [] # clear previous data
        for _ in range(self._number_of_elements):
            self._data.append(
                randint(self._min_element_value, self._max_element_value)   
            )
    
    # enforces the use of .sort() with subclass instantiations
    def sort(self):
        raise NotImplementedError("Error: need to use .sort()")

"""SelectionSort Class"""
class SelectionSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

    def sort(self) -> list:
        data = self._data
        n = len(data)
        # Iterates through the list of data, assume the first element is smallest
        steps = []

        # record method inside of sort to track sorting stages for front-end use later
        def record(i=None, j=None, action=None) -> None:
            steps.append({
                "array": data.copy(),
                "i": i,
                "j": j,
                "action": action
            })

        record(action="start")

        for i in range(n-1):
            min_index = i
            # Iterates through the unsorted remaining elements
            for j in range(i+1, n): 
                record(i=min_index,j=j,action="compare") #
                if data[j] < data[min_index]: # Found a smaller element
                    min_index = j # set to be new smallest
            
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i] #swap positions
                record(i=i,j=min_index,action="swap")
        record(action="done")
        return steps
    
"""BubbleSort Class"""
class BubbleSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

    def sort():
        pass

"ThreeWayMergeSort Class"
class ThreeWayMergeSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""BucketSort Class"""
class BucketSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""CountingSort Class"""
class CountingSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""CycleSort Class"""
class CycleSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""HeapSort Class"""
# may add HeapPriority class to also inherit from
class HeapSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value) 

"""InsertionSort Class"""
class InsertionSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""IntroSort Class"""
class IntroSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""MergeSort Class"""
class MergeSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""PigeonholeSort Class"""
class PigeonholeSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""QuickSort Class"""
class QuickSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""RadixSort Class"""
class RadixSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

"""TimSort Class"""
class TimSort(SortingAlgorithm):
    def __init__(self, num_elements=10, min_value=0, max_value=500) -> None:
        super().__init__(num_elements, min_value, max_value)

# Algorithm registry for main.py Flask use
ALGORITHMS = {
    "selection": SelectionSort,
    "bubble": BubbleSort,
    "merge": MergeSort,
    "tim": TimSort,
    "radix": RadixSort,
    "quick": QuickSort,
    "pigeonhole": PigeonholeSort,
    "merge": MergeSort,
    "intro": IntroSort,
    "insertion": InsertionSort,
    "heap": HeapSort,
    "cycle": CycleSort,
    "counting": CountingSort,
    "bucket": BucketSort,
    "three-way-merge": ThreeWayMergeSort
}
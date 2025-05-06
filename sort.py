import random
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class SortingAlgorithms:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

    def ai_select_sort(self, arr):
        X_train = np.array([[10, 0], [50, 0], [100, 0], [10, 1], [50, 1], [100, 1]])
        y_train = np.array(["Insertion", "Merge", "Merge", "Bubble", "Insertion", "Merge"])

        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)

        list_size = len(arr)
        sorted_check = int(arr == sorted(arr))
        prediction = model.predict([[list_size, sorted_check]])
        print(f"AI Selected Algorithm: {prediction[0]}")

        if prediction[0] == "Bubble":
            return self.bubble_sort(arr)
        elif prediction[0] == "Insertion":
            return self.insertion_sort(arr)
        else:
            return self.merge_sort(arr)

# Example usage
sorter = SortingAlgorithms()
arr = [random.randint(1, 1000) for _ in range(50)]
print("Original Array:", arr)
print("Bubble Sort:", sorter.bubble_sort(arr.copy()))
print("Insertion Sort:", sorter.insertion_sort(arr.copy()))
print("Merge Sort:", sorter.merge_sort(arr.copy()))
print("AI Chosen Sort:", sorter.ai_select_sort(arr.copy()))

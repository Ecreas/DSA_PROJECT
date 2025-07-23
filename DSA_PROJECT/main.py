import streamlit as st
import time
import copy


def bubble_sort(arr):
    n = len(arr)
    steps = 0
    arr = arr.copy()
    for i in range(n-1):
        for j in range(n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, steps


def merge_sort(arr):
    steps = [0]

    def merge_sort_rec(a):
        if len(a) > 1:
            mid = len(a)//2
            L = a[:mid]
            R = a[mid:]
            merge_sort_rec(L)
            merge_sort_rec(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                steps[0] += 1
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1

    arr_copy = arr.copy()
    merge_sort_rec(arr_copy)
    return arr_copy, steps[0]


st.title("Bubble Sort vs Merge Sort Comparison")

user_input = st.text_input("Enter elements of the array", "")

if user_input.strip() == "":
    st.info("Please enter data to see the algorithm results.")
    st.stop()

try:
    data = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
except:
    st.error("Please enter valid integers separated by commas.")
    st.stop()

st.session_state["input_data"] = data  

col1, col2 = st.columns(2)

with col1:
    st.header("Bubble Sort")
    arr = copy.deepcopy(data)
    start = time.perf_counter()
    sorted_arr, steps = bubble_sort(arr)
    elapsed = (time.perf_counter() - start) * 1000  
    st.write("Sorted:", sorted_arr)
    st.write("Steps:", steps)
    st.write(f"Time: {elapsed:.3f} ms")

with col2:
    st.header("Merge Sort")
    arr = copy.deepcopy(data)
    start = time.perf_counter()
    sorted_arr, steps = merge_sort(arr)
    elapsed = (time.perf_counter() - start) * 1000  # ms
    st.write("Sorted:", sorted_arr)
    st.write("Steps:", steps)
    st.write(f"Time: {elapsed:.3f} ms")
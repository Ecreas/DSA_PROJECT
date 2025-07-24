import streamlit as st
import time

st.title("Bubble Sort Visualization")

if "input_data" in st.session_state:
    data = st.session_state["input_data"]
else:
    st.warning("No input data found. Please enter data on the main page first.")
    st.stop()

st.subheader("Input Data")
st.bar_chart(data)


st.subheader("Bubble Sort Code")
st.code(
"""
void bubbleSort(int arr[], int numElements) {
    for (int i = 0; i < numElements - 1; i++) {
        for (int j = 0; j < numElements - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {          
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
""", language="cpp")



st.subheader("Step-by-Step Bubble Sort")

steps = []
arr = data.copy()
steps.append(arr.copy())  
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        steps.append(arr.copy())  

step_num = st.slider("Step", 0, len(steps)-1, 0)  
st.bar_chart(steps[step_num])

st.info(f"Showing step {step_num} of {len(steps)-1}")


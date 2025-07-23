import streamlit as st
import matplotlib.pyplot as plt



st.subheader("Merge Sort Code")
st.code(
"""
void merge(int leftArray[], int rightArray[], int array[], int leftSize, int rightSize) {
    int i = 0, l = 0, r = 0;

    while (l < leftSize && r < rightSize) {
        if (leftArray[l] < rightArray[r]) {
            array[i] = leftArray[l];
            i++;
            l++;
        } else {
            array[i] = rightArray[r];
            i++;
            r++;
        }
    }

    while (l < leftSize) {
        array[i] = leftArray[l];
        i++;
        l++;
    }

    while (r < rightSize) {
        array[i] = rightArray[r];
        i++;
        r++;
    }
}

void mergeSort(int array[], int length) {
    if (length <= 1) return;

    int middle = length / 2;
    int leftSize = middle;
    int rightSize = length - middle;

    int* leftArray = new int[leftSize];
    int* rightArray = new int[rightSize];

    int j = 0;
    for (int i = 0; i < length; i++) {
        if (i < middle) {
            leftArray[i] = array[i];
        } else {
            rightArray[j] = array[i];
            j++;
        }
    }

    mergeSort(leftArray, leftSize);
    mergeSort(rightArray, rightSize);
    merge(leftArray, rightArray, array, leftSize, rightSize);

    delete[] leftArray;
    delete[] rightArray;
}
""", language="cpp")




def plot_mergesort_tree(arr, x=1, y=1, dx=1, dy=1, ax=None, depth=0, max_depth=10):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        plot_mergesort_tree(arr, x, y, dx, dy, ax, 0, max_depth)
        st.pyplot(fig)
        return

    
    ax.text(x, y, str(arr), ha='center', va='center', bbox=dict(boxstyle="round", fc="w", ec="b"))
    if len(arr) > 1 and depth < max_depth:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        ax.plot([x, x - dx], [y , y - dy ], 'k-')
        ax.plot([x, x + dx], [y , y - dy ], 'k-')
        
        plot_mergesort_tree(left, x - dx, y - dy, dx / 2, dy, ax, depth + 1, max_depth)
        plot_mergesort_tree(right, x + dx, y - dy, dx / 2, dy, ax, depth + 1, max_depth)

if "input_data" in st.session_state:
    data = st.session_state["input_data"]
else:
    st.warning("No input data found. Please enter data on the main page first.")
    st.stop()

st.subheader("Input Data")
st.write(data)

st.subheader("Merge Sort Visualization Tree")
plot_mergesort_tree(data)

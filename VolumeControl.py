import streamlit as st

def VolumeControl():

    # Header
    st.title("AI Gesture Volume Control")
    st.write("---")

    # About the project
    st.header("Gesture-Based Volume Control Project")
    st.image("VolumeControl/1.jpg")

    st.markdown(
        """
        ### About the Project

        This AI-powered application allows users to control the system volume using hand gestures. By detecting the distance between specific hand landmarks (thumb and index finger), it maps the movement to adjust the volume dynamically.

        **Key Features:**
        - Real-time hand detection using MediaPipe.
        - Smooth volume control based on the distance between thumb and index finger.
        - Intuitive visual feedback with a volume bar.

        **Technologies Used:**
        - **OpenCV**: For video capture, frame processing, and rendering visual elements.
        - **MediaPipe**: For accurate hand tracking and landmark detection.
        - **NumPy**: For efficient numerical operations and interpolation.
        - **AppleScript** (macOS-specific): To control system volume programmatically.
        - **Streamlit**: To create an interactive interface.

        **How It Works:**
        1. The webcam captures the user’s hand in real-time.
        2. Detects key landmarks on the hand (e.g., thumb and index finger) using MediaPipe.
        3. Calculates the distance between the landmarks to determine the target volume.
        4. Dynamically adjusts the system volume using the computed value.

        **Use Cases:**
        - Hands-free volume adjustment for accessibility.
        - Gesture-based controls for multimedia systems.
        - Interactive systems and AR applications.

        """
    )

    st.write("---")

    # Contact
    st.header("Source Code and Project Links")
    st.write(
        """
        [Gesture Volume Control GitHub Repository](https://github.com/MaryamMaksour/Computer_Vision/tree/main/Gesture%20Volume%20Control)
        """
    )



if __name__ == "__VolumeControl__":
    VolumeControl()
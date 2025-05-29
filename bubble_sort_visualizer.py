import cv2
import numpy as np
import os

def draw_bars(img, data, highlight_indices=None, text=""):
    width, height = 800, 720
    margin = width // 6
    bar_width = 60
    spacing = 30
    
    img.fill(255)
    
    for i, value in enumerate(data):
        x = margin + i * (bar_width + spacing)
        y = height - margin
        bar_height = int((value / max(data)) * (height - 2 * margin - 100))
        
        if highlight_indices and i in highlight_indices:
            color = (0, 0, 255)  # Red
        else:
            color = (100, 200, 100)  # Light green
        
        cv2.rectangle(img, (x, y), (x + bar_width, y - bar_height), color, -1)
        cv2.putText(img, str(value), (x + 15, y + 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    
    cv2.putText(img, "Bubble Sort Visualization", (width//6, 40), 
               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 200), 2)
    cv2.putText(img, text, (width // 6, 80), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    return img

def save_bubble_sort_video(data, output_path, fps=2):
    width, height = 800, 720
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    img = np.ones((height, width, 3), np.uint8) * 255
    arr = data.copy()
    n = len(arr)
    
    # Add initial frame
    text = "Original data before sorting begins"
    img = draw_bars(img, arr, None, text)
    for _ in range(fps * 2):  # Show for 2 seconds
        video_writer.write(img)
    
    for i in range(n):
        text = f"Outer loop pass #{i+1} through the array"
        img = draw_bars(img, arr, None, text)
        for _ in range(fps * 1):  # Show for 1 second
            video_writer.write(img)
        
        for j in range(0, n-i-1):
            text = f"Comparing {arr[j]} (index {j}) with {arr[j+1]} (index {j+1})"
            img = draw_bars(img, arr, [j, j+1], text)
            for _ in range(fps * 1):  # Show for 1 second
                video_writer.write(img)
            
            if arr[j] > arr[j+1]:
                text = f"Since {arr[j]} > {arr[j+1]} (TRUE) - will swap"
                img = draw_bars(img, arr, [j, j+1], text)
                for _ in range(fps * 1):  # Show for 1 second
                    video_writer.write(img)
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                text = f"Swapped: {arr[j]} at index: {j}, {arr[j+1]} at index: {j+1}"
                img = draw_bars(img, arr, [j, j+1], text)
                for _ in range(fps * 2):  # Show for 2 seconds
                    video_writer.write(img)
            else:
                text = f"Since {arr[j]} <= {arr[j+1]} (FALSE) - no swap"
                img = draw_bars(img, arr, [j, j+1], text)
                for _ in range(fps * 1):  # Show for 1 second
                    video_writer.write(img)
    
    # Add final frame
    text = "Sorting complete! Array is now sorted."
    img = draw_bars(img, arr, None, text)
    for _ in range(fps * 3):  # Show for 3 seconds
        video_writer.write(img)
    
    video_writer.release()
    print(f"Video saved successfully at: {os.path.abspath(output_path)}")

# Example usage
data = [7, 2, 5, 4, 1, 3]
output_path = "bubble_sort_visualization.mp4"  # Change this to your desired path
save_bubble_sort_video(data, output_path, fps=2)

# **Automated Sanitizer Dispenser and Mask Detector**  

### **Overview**  
This project combines **computer vision** and **embedded systems** to automate **mask detection** and **sanitizer dispensing**, aimed at minimizing the spread of COVID-19. It integrates **deep learning-based face mask detection** with an **Arduino-controlled IR sensor** to ensure contactless hand sanitization.  

### **Key Features**  
- **Mask Detection Model:** Developed a **Convolutional Neural Network (CNN)** using **TensorFlow, Keras, and OpenCV**, achieving **96% recall** in identifying mask usage.  
- **Dataset & Augmentation:** Trained on **800+ images** (50% masked, 50% unmasked) and enhanced with **data augmentation techniques** for improved generalization.  
- **Face Detection:** Utilized **Haar Cascade Classifier** for accurate real-time face detection before applying mask classification.  
- **Automated Sanitizer Dispensing:** Integrated an **Arduino** with **IR sensors** to dispense sanitizer only when a person is detected without a mask, ensuring a contactless and efficient solution.  
- **Overfitting Prevention:** Implemented **dropout regularization** and **batch normalization**, achieving **98% training accuracy** while maintaining robustness.  

### **Tech Stack**  
- **Languages & Frameworks:** Python, TensorFlow, Keras, OpenCV, Arduino C++  
- **Hardware:** Arduino, IR Sensors, Servo Motor  
- **Tools:** Jupyter Notebook, Haar Cascade, NumPy, Pandas  

### **Results & Insights**  
- The model demonstrated **high accuracy and recall**, ensuring reliable mask detection in real-world scenarios.  
- The **automated dispensing mechanism** provided an efficient, **contact-free hygiene solution**, reducing manual intervention.  
- Combining **machine learning with embedded systems** showcased a practical approach to **public health automation**.  

### **Future Enhancements**  
- Implement **edge AI optimization** using TensorFlow Lite for **real-time inference on low-power devices**.  
- Improve face detection with **deep learning-based detectors** like MTCNN or SSD.  
- Add **temperature screening** for enhanced COVID-19 safety measures.  


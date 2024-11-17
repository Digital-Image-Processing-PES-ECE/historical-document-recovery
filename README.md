# Historical Document Recovery

### Project Description:
Recovering texts and images from historical documents like old books and manuscripts is a critical task in preserving cultural and historical heritage. These documents often suffer from physical degradation, such as fading ink, torn pages or environmental damage. 
Advanced image processing techniques help overcome these challenges, enabling clearer analysis and digital preservation. 
Such processes not only preserve the textual content but also provide researchers with digital access to materials previously limited to physical archives, making historical insights accessible for education and study.

#### Summary - 
This project helps to process an image to enhance text visibility, making it suitable for tasks like Optical Character Recognition (OCR) or visual analysis. The pipeline involves grayscale conversion, noise reduction, contrast enhancement, and adaptive thresholding. These steps work together to handle uneven lighting, degraded text, and noise, often seen in scanned documents or historical manuscripts. The result is a clean, high-contrast binary image suitable for text extraction or further analysis.

#### Course concepts used - 
1. Contrast Modification
2. Binary Thresholding
3. Image Binarization
4. Noise Reduction
5. Edge Detection

#### Novelty - 
1. Analysing old text
2. Digital Preservation
   
### Contributors:
1. Bhaviksha N (PES1UG22EC054)
2. Myla Kinnera Sri (PES1UG22EC904)

### Steps:
1. Clone Repository
```git clone https://github.com/Digital-Image-Processing-PES-ECE/historical-document-recovery.git ```

2. Install Dependencies
```pip install -r requirements.txt```

3. Run the Code
```python main.py (for eg.)```

### References:
1. https://www.textmanuscripts.com/medieval/book-of-hours-use-of-bourges-204456?inventorySearch=0&p=49
2. https://www.lesenluminures.com/artworks/categories/11/9822-choir-gradual-with-feasts-for-the-temporal-franciscan-piedmont-northern-italy-c.-1450-1460/
3. https://www.lesenluminures.com/artworks/10023-book-of-hours-use-of-venice-italy-venice-1442-dated/
4. https://www.textmanuscripts.com/medieval/choir-book-antiphonal-127692
5. https://art.thewalters.org/detail/78370/leaf-from-book-of-hours-27/
   
### Limitations and Future Work:
The fine text is faint and challenging to detect accurately.

It can be utilized to extract text through Optical Character Recognition (OCR), machine learning models, or a combination of both, enabling more effective analysis and enhanced results.

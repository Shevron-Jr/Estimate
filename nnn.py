import fitz  # PyMuPDF
import cv2
import numpy as np
from shapely.geometry import Polygon, Point

def extract_page_image(pdf_path, page_number, output_image_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number - 1)  # page_number is 1-based index
    pix = page.get_pixmap()
    pix.save(output_image_path)
    return output_image_path

def process_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return edges

def find_contours(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def calculate_area(contour, scale_factor):
    polygon = Polygon([point[0] for point in contour])
    area_in_sq_inches = polygon.area
    area_in_sq_feet = area_in_sq_inches / (scale_factor ** 2)
    return area_in_sq_feet

def identify_rooms_by_geometry(contours):
    rooms = []
    for contour in contours:
        if len(contour) >= 4:  # Ensure the contour has at least 4 points
            polygon = Polygon([point[0] for point in contour])
            if polygon.area > 1000:  # Example threshold to filter out small contours
                rooms.append({'name': 'Room', 'contour': contour})
    return rooms

def main():
    pdf_path = '/Users/oluwasegunmohammed/Downloads/Peterson BIDDING Plans 4.4.24.pdf'
    page_number = 7  # Sheet A101
    output_image_path = 'page7.png'
    
    # Input scale: for example, 1/8 inch equals 1 foot, you would input 8
    scale_input = 8
    scale_factor = scale_input  # 1/scale_input inch equals 1 foot
    
    # Step 1: Extract the page image
    image_path = extract_page_image(pdf_path, page_number, output_image_path)
    
    # Step 2: Process the image to detect edges
    edges = process_image(image_path)
    
    # Step 3: Find contours
    contours = find_contours(edges)
    
    # Step 4: Identify rooms by geometry
    rooms = identify_rooms_by_geometry(contours)
    
    # Step 5: Calculate areas for each identified room
    for room in rooms:
        area_in_sq_feet = calculate_area(room['contour'], scale_factor)
        print(f"Room: {room['name']}, Area: {area_in_sq_feet:.2f} square feet")

if __name__ == "__main__":
    main()

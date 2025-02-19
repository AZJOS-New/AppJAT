import cv2
from pyzbar.pyzbar import decode

# Cargar una imagen desde un archivo
image_path = "qr_code.png"  # Cambia esto por la ruta de tu imagen
image = cv2.imread(image_path)

# Decodificar códigos QR en la imagen
decoded_objects = decode(image)
for obj in decoded_objects:
    print("Código QR detectado:", obj.data.decode("utf-8"))

    # Dibujar un rectángulo alrededor del código QR
    points = obj.polygon
    if len(points) > 4:
        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
        cv2.polylines(image, [hull], True, (0, 255, 0), 2)
    else:
        cv2.polylines(image, [np.array(points)], True, (0, 255, 0), 2)

# Mostrar la imagen con el código QR detectado
cv2.imshow("Imagen con QR", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
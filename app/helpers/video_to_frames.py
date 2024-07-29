import os
import cv2


def video_to_frames(file_path, output_folder):
    
    # Abre o vídeo
    cap = cv2.VideoCapture(file_path)

    # Verifica se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Cria o output_folder se ele não existir
    if not os.path.exists("files/frames_folder"):
        os.makedirs("files/frames_folder")

    if not os.path.exists(f"files/frames_folder/{output_folder}"):
        os.makedirs(f"files/frames_folder/{output_folder}")


    # Loop para ler os frames do vídeo e salvá-los como imagens
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Salva o frame como imagem
        image_path = os.path.join(f"{output_folder}", f"frame_{frame_count}.jpg")
        cv2.imwrite(image_path, frame)

        frame_count += 1

    # Fecha o vídeo
    cap.release()

    print(f"{frame_count} frames extraídos com sucesso.")


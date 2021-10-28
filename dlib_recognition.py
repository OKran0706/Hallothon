import dlib
import matplotlib.pyplot as plt
import numpy as np
import speak

def match_face(image1, image2):
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")
    model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

    img1_path = image1
    img2_path = image2

    img1 = dlib.load_rgb_image(img1_path)
    img2 = dlib.load_rgb_image(img2_path)

    img1_detected = detector(img1, 1)
    img2_detected = detector(img2, 1)
    try:
        img1_shape = sp(img1, img1_detected[0])
        img2_shape = sp(img2, img2_detected[0])
    
    except:

        speak.speak_text("No known face detected")
        exit()

    img1_aligned = dlib.get_face_chip(img1, img1_shape)
    img2_aligned = dlib.get_face_chip(img2, img2_shape)

    img1_representation = model.compute_face_descriptor(img1_aligned)
    img2_representation = model.compute_face_descriptor(img2_aligned)

    img1_representation = np.array(img1_representation)
    img2_representation = np.array(img2_representation)

    def findEuclideanDistance(source_representation, test_representation):
        euclidean_distance = source_representation - test_representation
        euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
        euclidean_distance = np.sqrt(euclidean_distance)
        return euclidean_distance

    distance = findEuclideanDistance(img1_representation, img2_representation)

    threshold = 0.6

    if distance < threshold:
        return True
    else:
        return False




import tensorflow
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input


# Create a resnet model
# weights are trained from the ImageNet dataset
# include_top is False as we will add our own top layer
# input shape of images is resized to (224, 224, 3)
resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
resnet.trainable = False

resnet = tensorflow.keras.Sequential([
    resnet,
    GlobalMaxPooling2D()
])

# print(resnet.summary())


# Function to extract features from an input uploaded/provided by the user
def extract_image_features(input_path, model):

    # Get the image from the input path
    img = image.load_img(input_path, target_size=(224, 224))

    # Convert the image to a numpy array
    img_array = image.img_to_array(img)

    # Reshape the image as Keras works on batch of images.
    # Even if we have 1 image we need to show Keras that it is a batch with 1 image
    expanded_img_array = np.expand_dims(img_array, axis=0)

    # Preprocess the image to match ResNet expected format as per the ImageNet dataset
    preprocessed_img_array = preprocess_input(expanded_img_array)

    # Extract the features from the image using the ResNet model
    # Flatten it so that it becomes a 1-D vector of size 2048
    result = model.predict(preprocessed_img_array).flatten()

    # Normalize the
    normalized_result = result / norm(result)

    return normalized_result

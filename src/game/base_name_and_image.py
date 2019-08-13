class BaseClassForNameAndImage(object):

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def get_name(self):
        """
        Returns
            str: the name
        """
        return self.name

    def get_image(self):
        """
        Returns
            str: the image
        """
        return self.image

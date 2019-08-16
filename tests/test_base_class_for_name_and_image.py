from src.game.base_name_and_image import BaseClassForNameAndImage


def test_base_class_for_name_and_image_has_name():
    base_class = BaseClassForNameAndImage(name='Name', image='Image')
    assert base_class.get_name() == 'Name'


def test_base_class_for_name_and_image_has_image():
    base_class = BaseClassForNameAndImage(name='Name', image='Image')
    assert base_class.get_image() == 'Image'

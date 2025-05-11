import pytest
import string
from password_generator import generate_password, check_password_strength

def test_password_length():
    password = generate_password(length=12)
    assert len(password) == 12

def test_password_too_short():
    with pytest.raises(ValueError, match="Длина пароля должна быть не менее 4 символов!"):
        generate_password(length=3)

def test_no_character_sets():
    with pytest.raises(ValueError, match="Необходимо выбрать хотя бы один набор символов!"):
        generate_password(length=8, use_uppercase=False, use_lowercase=False, use_digits=False, use_special=False)

def test_password_strength_strong():
    password = generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
    assert check_password_strength(password) == "Сильный"
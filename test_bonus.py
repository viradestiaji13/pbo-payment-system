import pytest
from core.base import PaymentMethod
from core.registry import buat_metode

def test_payment_methode_is_abstract():
    """Memastikan Abstract Base Class PaymentMethode tidak bisa diinstansiasi langsung."""
    with pytest.raises(TypeError):
        PaymentMethod("Test Abstract")

def test_unknown_plugin_raises_keyerror():
    """Memastikan plugin yag tidak terdaftarmemunculkan KeyError."""
    with pytest.raises(KeyError):
        buat_metode("plugin_palsu")

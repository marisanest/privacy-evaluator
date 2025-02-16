import pytest

from privacy_evaluator.attacks.attack import Attack
from privacy_evaluator.models.torch.dcti.dcti import load_dcti
from privacy_evaluator.datasets.cifar10 import CIFAR10
from privacy_evaluator.classifiers.classifier import Classifier


def test_attack():
    x_train, y_train, x_test, y_test = CIFAR10.numpy()
    target_model = Classifier(
        load_dcti(), nb_classes=CIFAR10.N_CLASSES, input_shape=CIFAR10.INPUT_SHAPE
    )
    attack = Attack(target_model, x_train, y_train, x_test, y_test)
    with pytest.raises(NotImplementedError):
        attack.attack()

from privacy_evaluator.attacks.membership_inference.black_box_rule_based import (
    MembershipInferenceBlackBoxRuleBasedAttack,
)
from privacy_evaluator.models.torch.dcti.dcti import load_dcti
from privacy_evaluator.datasets.cifar10 import CIFAR10
from privacy_evaluator.classifiers.classifier import Classifier


def test_membership_inference_black_box_rule_based_attack():
    x_train, y_train, x_test, y_test = CIFAR10.numpy()
    target_model = Classifier(
        load_dcti(), nb_classes=CIFAR10.N_CLASSES, input_shape=CIFAR10.INPUT_SHAPE
    )
    attack = MembershipInferenceBlackBoxRuleBasedAttack(
        target_model, x_train[:100], y_train[:100], x_test[:100], y_test[:100]
    )
    attack.attack()

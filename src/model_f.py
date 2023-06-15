from __future__ import annotations
import collections
from dataclasses import dataclass, asdict
from typing import Optional, List, Counter
import weakref
import sys


@dataclass(frozen=True)
class Sample:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@dataclass(frozen=True)
class KnownSample(Sample):
    species: str


@dataclass
class TestingKnownSample:
    sample: KnownSample
    classification: Optional[str] = None


@dataclass(frozen=True)
class TrainingKnownSample:
    """주의: classification 인스턴스 변수를 사용할 수 없다."""
    sample: KnownSample


@dataclass
class UnknownSample:
    sample: Sample
    classification: Optional[str] = None


class Distance:
    """거리 계산의 추상적 정의"""
    def distance(self, s1: Sample, s2: Sample) -> float:
        raise NotImplementedError
    

@dataclass
class Hyperparameter:
    """k 및 거리 계산 알고리즘이 있는 튜닝 매개변수 집합"""
    k: int
    algorithm: Distance
    data: weakref.ReferenceType["TrainingData"]

    def classify(self, unknown: Sample) -> str:
        """k-NN 알고리즘"""
        if not (training_data := self.data()):
            raise RuntimeError("No TrainingData object")
        distances: list[tuple[float, TrainingKnownSample]] = sorted(
            (self.algorithm.distance(unknown, known.sample), known)
            for known in training_data.training
        )
        k_nearest = (known.sample.species for d, known in distances[: self.k])
        frequency: Counter[str] = collections.Counter(k_nearest)
        best_fit, *others = frequency.most_common()
        species, votes = best_fit
        return species
    

@dataclass
class TrainingData:
    testing: List[TestingKnownSample]
    training: List[TrainingKnownSample]
    tuning: List[Hyperparameter]


# Special case, we don't *often* test abstract superclasses.
# In this example, however, we can create instances of the abstract class.
test_Sample = """
>>> x = Sample(1, 2, 3, 4)
>>> x
Sample(sepal_length=1, sepal_width=2, petal_length=3, petal_width=4)
"""

test_TrainingKnownSample = """
>>> s1 = TrainingKnownSample(
...     sample=KnownSample(
...         sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa"
...     )
... )
>>> s1
TrainingKnownSample(sample=KnownSample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='Iris-setosa'))
# 이것은 바람직하지 않다...
>>> s1.classification = "wrong"
Traceback (most recent call last):
...
dataclasses.FrozenInstanceError: cannot assign to field 'classification'
>>> hash(s1) is not None
True
"""

test_TestingKnownSample = """
>>> s2 = TestingKnownSample(
...     KnownSample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa"),
...     classification=None
... )
>>> s2
TestingKnownSample(sample=KnownSample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='Iris-setosa'), classification=None)
# 예상 결과는 다음과 같다...
>>> s2.classification = "wrong"
>>> s2
TestingKnownSample(sample=KnownSample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='Iris-setosa'), classification='wrong')
"""

test_UnknownSample = """
>>> u = UnknownSample(
...     sample=Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2), 
...     classification=None)
>>> u
UnknownSample(sample=Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2), classification=None)
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
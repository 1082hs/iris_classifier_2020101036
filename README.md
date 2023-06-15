# 아이리스 꽃종 분류기
 해당 코드는 꽃 받침의 길이(sepal_length)와 너비(sepal_width) 그리고 꽃잎의 길이(petal_length)와 너비(petal_width)에 따라 붓꽃의 종류를 구분하는 것이다.
 종류는 다음의 세 가지 종류로 나뉜다. Iris setosa(세토사), Iris virginica(버지니카), Iris versicolor(베르시칼라)

Sample: 샘플 데이터를 나타내는 클래스로 sepal_length, sepal_width, petal_length, petal_width의 속성을 가진다.

KnownSample: 분류 정보를 포함하는 샘플 데이터를 나타내는 클래스로 sample 속성은 Sample 클래스의 인스턴스를 가지고 있고, species 속성은 해당 샘플의 종(species)을 나타낸다.

TestingKnownSample: 테스트용으로 사용되는 KnownSample의 하위 클래스이다. sample 속성은 테스트용 샘플 데이터를 나타내고, classification 속성은 해당 샘플의 분류 결과를 나타낸다.

TrainingKnownSample: 훈련 데이터로 사용되는 KnownSample의 하위 클래스이며 sample 속성은 훈련용 샘플 데이터를 나타낸다.

UnknownSample: 분류되지 않은 샘플 데이터를 나타내는 클래스이고, sample 속성은 Sample 클래스의 인스턴스를 가지고 있고, classification 속성은 해당 샘플의 분류 결과를 나타낸다.

Distance: 거리 계산을 위한 추상 클래스이다. distance 메서드는 두 개의 샘플을 입력으로 받아 거리를 계산하는 역할을 하고, 이 클래스를 상속받아 구체적인 거리 계산 알고리즘을 구현해야 한다.

Hyperparameter: k-NN 알고리즘의 하이퍼파라미터인 k와 거리 계산 알고리즘을 포함하는 클래스이며 classify 메서드는 주어진 샘플을 분류하는 역할을 한다.

TrainingData: 훈련 데이터, 테스트 데이터, 하이퍼파라미터 튜닝 데이터를 관리하는 클래스이다.


# 소감
파이썬에 거의 무지한 상태로 시작해서 솔직하게 어렵게 느껴졌습니다.
그런데 교수님께서 저희를 많이 신경 써 주시고, 친절하게 설명해주셔서
조금씩 감이 잡혀가게 되었습니다.
강의 중에 진로와 관련해서 다양한 얘기를 해주셔서 감사하고 소중한 말씀이라고 생각합니다.
제가 관련 지식이 많이 부족해서 강의를 많이 못 따라간게 너무 아쉽지만
그래도 어느 정도 배워간다는 느낌이 들어 너무 좋습니다.
이 강의를 계기로 더욱 성장해나가겠습니다.
한 학기동안 감사했습니다!
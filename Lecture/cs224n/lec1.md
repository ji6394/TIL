Lecture1 : Introduction and Word Vectors
1. The course
2. Human language and word meaning
- complex
- 각자 다르게 해석함
- 언어는 사람이 만든 체계
- 언어는 등장한지 그래 오래 되지 않음
- 컴퓨터가 어떻게 사람의 말을 이해하게 할지를 설계하는 것
- Machine translation은 굉장히 발달함
- GPT-3는 OPEN AI에서 만든 굉장한 거대 언어 모델. 이전의 단어를 기반으로 다음 단어를 예측함.
- (~16:20)
- Wordnet같은 resource들의 문제점
- - 뉘앙스를 이해하지 못함
- - 단어의 신의미를 이해하지 못함
- - 비슷한 단어 간의 차이를 이해하지 못함
- 과거의 NLP에서는 단어가 discrete symbols로 인식됨. 원핫벡터를 사용함. Vocabulary의 사이즈가 너무 커짐.
- 단어 간의 similarity와 관계를 파악하지 못함
- orthogonal : 직교의
- 이를 해결하기 위해 현대의 nlp 기법들 등장
- 그 첫번째가 distributional semantics : 단어의 의미는 그 단어에 빈번하게 근접하게 나타나는 다른 단어들에 의해 부여됨. context words라고 하죠. 
- nlp에서 단어들은 types와 tokens로 분류될 수 있음
- distributional semantics를 통해 각 단어의 dense한 real vector를 얻어냄. 비슷한 단어끼리 embedding이 모여있게 됨. 
3. Word2vec Introduction
- corpus 내의 각 단어를 벡터로 표현. 모든 위치마다 target word와 context words간의 word vector의 similarity를 이용하여 해당 단어가 등장할 확률을 계산하고 확률을 최대화하기 위해 word vector를 계속해서 변경하는 과정. 
- Corpus에서 각 단어의 위치인 t마다 target word로 설정. 이에 따라 context words를 예측. window size는 m으로 설정. Data Likelihood = L(theta) = 각 자리별로 target word를 옮겨가며 target word가 등장했을 때 window size내 context word의 확률을 모두 곱함.
이에 따른 Objective Function(cost function, loss function)은 극대화하는 것이 아니라 극소화해야 전체 정확도가 높아지기 때문에 앞에 -가 붙음. 또한 곱보다 합을 다루는 것이 편하기에 log를 붙힘.
(~33:00)
4. Word2vec objectvie function gradietns
5. Optimization basics
6. Looking at word vectors


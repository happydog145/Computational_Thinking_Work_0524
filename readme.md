# 에라토스테네스의 체:
소수를 판별하는 알고리즘이다.

소수들을 대량으로 빠르고 정확하게 구하는 방법이다.

단일 숫자 소수 여부 확인
어떤 수의 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.

수가 수(N이라고 가정)를 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.

만약, 대량의 소수를 한꺼번에 판별해야할 경우는 '에라토스테네스의 체'를 이용한다.

에라토스테네스의 체 원리
에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 배열을 할당하여, 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.

배열을 생성하여 초기화한다.
2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)
2부터 시작하여 남아있는 수를 모두 출력한다.

# 코드에 사용한 방법:
에라토스테네스의 체 알고리즘을 통해 max 값인 3000까지의 소수를 모두 판별한 후,
간단하게 값을 입력하면 bool 값을 얻을 수 있도록 하였다.

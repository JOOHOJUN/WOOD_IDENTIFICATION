PyQT5로 만든 간단한 python UI입니다.

문제가 주어지고 답을 입력+엔터하면 정답이 보입니다. 다음 버튼으로 다음 문제로 넘어갑니다. 끝에 도달하면 끝입니다를 출력합니다.
이때 다시 다음 누르면 처음부터 다시 시작합니다.

textBrowser는 content와 result로 나뉘고 
pushButton을 클릭할 때마다 content가 갱신됩니다.
result는 lineEdit에서 returnPressed 반응이 있으면 출력됩니다.

2017.08.06 version0.1

data_.py가 추가됩습니다. 이차원 리스트 형식이고 data_handler는 리스트 속 리스트를 가져와 저장합니다.
데이터 추가가 용이하고 원하는 데이터만 가져오고자 리스트 형식으로 만들어놨습니다.

데이터에는 국산침엽수 대상 정보만 있습니다.
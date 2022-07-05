

## ai studio System Action 개발 방법

# FormAction - Basics
# 공식문서 : https://legacy-docs-v1.rasa.com/core/forms/#form-basics
#  rasa_sdk.forms.FormAction 상속

# 필수 메서드
def 액션의이름(self) -> Text:
    """Unique identifier of the form"""
    return "user_infor_form"

@staticmethod
def required_slots(tracker: Tracker) -> List[Text]:
    """A list of required slots that the form has to fill"""
    return ['이름', '휴대폰번호']
  # required_slots : submit method를 실행하기 위해 필요한 slot 목록

# submit : slot이 모두 채워졌을 때 실행되는 메서드
def submit(self, 
          dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]
          ) -> List[Dict]:
  # slot name과 다음 메서드로 slot value를 가져올 수 있다.
    name = tracker.get_slot('이름')
    phonenum = tracker.get_slot('휴대폰번호')

    # ...(중략)...

  # db에 저장 (레거시 생략)

    dispatcher.utter_message(f'[예약번호: {reservNum}]\n{name} 고객님 예약 완료되었습니다. 저희 호텔을 이용해주셔서 감사합니다.')

    return []



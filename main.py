# Action
# rasa_sdk.Action 상속
# 필수 메서드 1. name : 액션의 이름 2. run:실행되는 메서드

def name(self) -> Text:
    """Unique identifier of the form"""
    return "action_reset_slot"

def run(self, dispatcher, tracker, domain, ):
    if tracker.latest_message['intent'].get('name') == 'reset':
      # 이 tracker에서 가장 최근 메세지 인텐트가 reset이라는 이름이면
      #  reset slot without name, phone number
        name = tracker.get_slot('이름')
        phonenum = tracker.get_slot('휴대폰번호')
        AllSlotsReset() #모든 slot을 none으로..
        dispatcher.utter_message(f'무엇이 궁금하신가요?') #추가로 궁금한걸 묻고 이름과 폰번호를 일단 가져가 모든대화가 끝난게 아니니까.
        return [SlotSet('이름', name), SlotSet('휴대폰번호', phonenum)]  
    else: # self.from_intent(intent='fine', value=True)
        dispatcher.utter_message('네 감사합니다. 즐거운 여행 되시기 바랍니다.')
    return [AllSlotsReset()] #대화종료하니까 모든slot을 지워.

# form은 아니지만 조금 복잡한 내용이 들어가야할 때 or 코드상의 필요가 있을 때 쓰는 action
# FormAction - Advanced
# Custom slot mappings
# 공식문서: https://legacy-docs-v1.rasa.com/core/forms/#custom-slot-mappings
# 엔티티 이름과 동일한 이름의 슬롯이 채워지도록 하는것이 기본.
# 다른 엔티티 혹은 특정 인텐트에서만 슬롯이 채워지도록 만들 수 있음. (엔티티이름과 슬롯이름이 다를경우?)
## 종류
# self.from_entity(entity-entity_name, intent=intent_name, role-role_name, group=group_name)
# self.from_intent(intent=intent_name, value=value) 
# self.from_trigger_intent(intent=intent_name, value=value)
# self.from_text(intent_name) -> 입력으로 들어온 값을 다 value로 받고 싶을 때 사용

def slot_mappings(self) -> Dict[Text, Any]:
    return {"이름": self.from_entity(entity='이름'),
           "휴대폰번호": self.from_entity(entity='휴대폰번호')}
  # 이건 엔티티이름과 슬롯이름이 동일한 경우야
# 숫자같은경우 카드번호나 계좌번호가 형식이 일정해서 다른 인텐트로 인식할수도 있으니까
# intent에 제한을 두면 좀 더 정확하게 받을 수 있음

### Custom request sentence for next slot
# 다음 slot을 요청하는 문장을 커스터마이즈하거나 사전에 등록된 slot 기반으로 검증할 수 있는 메서드

def request_next_slot(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[List[EventType]]:
    for slot in self.required_slots(tracker):
        if self._should_request_slot(tracker, slot):
            if slot == "침대종류":
                room_type = tracker.get_slot('객실종류')
                buttons = []
                # ...(생략)...
              dispatcher.utter_message(text='침대 종류를 선택해주세요', buttons=buttons)
              return [SlotSet{REQUESTED_SLOT, slot}]
            else:
                ## For all other slots, continue as usual
                dispathcer.utter_message(
                  template=f"utter_ask_{slot}", **tracker.slots
                )  
                return [SlotSet(REQUESTED_SLOT, slot)]
    return None
# 단순히 텍스트라면 utter_ask_slot_name으로 스튜디오에서 만들면 되는데 이것처럼 침대종류에 따라 내용을 바꾸고 싶거나 레거시로 도메인 정보가 필요할 때 이 방식으로 하면됨.
# request slot이면, 그 침대종류면 객실종류에 따라서 메시지 종류를 다르게 해라? 이 침대종류가 아닐경우 tracker.slot하면 기존에 등록되어있는 utter_ask_{slot}를 다 사용할수있어......무슨말이야

#########################3
# Validating user input : https://legacy-docs-v1.rasa.com/core/forms/#validating-user-input
# 사용자 입력을 검증하는 메서드 : validate_[slot_name] 형식
# 이 메서드 사용시 slot mapping에 self.from_text()를 같이 써주는 것을 권장
# 엔티티와 동일한 엔티티의 슬랏을 쓰면(해당엔티티가 안들어오면) 이것을 거치지 않고 바로 fallback.
# ex) 이름을 받는 내용인데 이름과 유사한 형태가 아닐경우 validate안거치고 fallback
# 근데 거치고 싶다면 validate_[slot_name] 쓰면 돼

def validate_구매량(self,
                 value: Text,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any],
                  ) -> Dict[Text, Any]:
    if int(value) > 10:
        dispatcher.utter_message(text='해당 상품은 10갸까지만 구매하실 수 있습니다.')
          return {"구매량": None}
    return {"구매량": value}


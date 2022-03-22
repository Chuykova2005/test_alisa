from requests import post

# print(post('http://localhost:5000/api/post',
#            json={"request": {},
#   "session": {
#     "session_id": "2eac4854-fce721f3-b845abba-20d60",
#     "message_id": 4,
#     "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#   },
#   "version": "1.0"}).json())

# тестирование первого входа на навык

# print(post('http://localhost:5000/api/post',
#    json={"request": {
#     "command": "закажи пиццу на улицу льва толстого, 16 на завтра",
#     "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра"
#   },
#   "session": {
#     "new": False,
#     "message_id": 4,
#     "session_id": "2eac4854-fce721f3-b845abba-20d60",
#     "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#     "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#   },
#   "version": "1.0"}).json())


# print(post('http://localhost:5000/api/post',
#    json={"request": {
#     "command": "ни за что",
#     "original_utterance": "ни за что"
#   },
#   "session": {
#     "new": False,
#     "message_id": 4,
#     "session_id": "2eac4854-fce721f3-b845abba-20d60",
#     "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#     "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#   },
#   "version": "1.0"}).json())

print(post('http://localhost:5000/api/post',
   json={"request": {
    "command": "хорошо",
    "original_utterance": "хорошо"
  },
  "session": {
    "new": False,
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
  },
  "version": "1.0"}).json())

